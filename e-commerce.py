import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with my Service Account File
cred = credentials.Certificate("/Users/zhangying-macbookpro/Documents/BYU-Pathway/BYU_Idaho/fall 2024/cse310/jianjun-furniture-store-firebase-adminsdk-dja2z-033eeb3f54.json")

firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Function to add data into Firestore
def add_product_to_category(category_name, product_id, name, price, stock):
    # Reference to the category subcollection within the products collection
    category_ref = db.collection('products').document(category_name).collection('category').document('product_id')
    #Set product details under the category subcollection
    category_ref.set({
        'name': name,
        'price': price,
        'stock': stock
    })
    print(f'Product {name} added under {category_name} successfully!')

def add_user(user_id, name, email):
    db.collection('users').document(user_id).set({
        'name': name,
        'email': email
    })
    print(f'User {name} added successfully!')

# merge new fields into existing document
def merge_field_user(user_id, name, email):
    db.collection('users').document(user_id).set({
        'new_user': True}, merge=True)


# Function to retrieve all documents from a collection
def get_products():
    products = db.collection('products').stream()
    for product in products:
        print(f'{product.id} => {product.to_dict()}')

def get_users():
    users = db.collection('users').stream()
    for user in users:
        print(f'{user.id} => {user.to_dict()}')

# Function to retrieve single document data from Firestore
def get_product():
    p001 = db.collection('products').document('P001').get()
    if p001.exists:
        print(f"P001: {p001.to_dict()}")
    else:
        print("Product does not exist!")

#Funciton to filter a collection
def filter_products():
    expensive_products = (
        db.collection("products")
        .where("price", ">=", 1000)
        .stream()
    )
    for ex in expensive_products:
        print(f"{ex.id} => {ex.to_dict()}")
#Function to order documents in a collection
def order_products():
    ordered_products = db.collection("products").order_by('price', direction = firestore.Query.DESCENDING).order_by('stock', direction = firestore.Query.DESCENDING).stream()
    for product in ordered_products:
        print(f'{product.id} => {product.to_dict()}')


# Function to update data in Firestore
def update_product(product_id, updated_data):
    db.collection('products').document(product_id).update(updated_data)
    print(f'Product {product_id} updated successfully!')

def update_user(user_id, updated_data):
    db.collection('users').document(user_id).update(updated_data)
    print(f'User {user_id} updated successfully!')

# Function to delete data from Firestore
def delete_product(product_id):
    db.collection('products').document(product_id).delete()
    print(f'Product {product_id} deleted successfully!')

def delete_user(user_id):
    db.collection('users').document(user_id).delete()
    print(f'User {user_id} deleted successfully!')

# Example usage
if __name__ == '__main__':
# Adding products to Firestore with their respective categories
# Living Room Products
    add_product_to_category("living_room", "lr1", "Sofa", 800, 15)
    add_product_to_category("living_room", "lr2", "Coffee Table", 150, 25)
    add_product_to_category("living_room", "lr3", "TV Stand", 200, 10)
    add_product_to_category("living_room", "lr4", "Bookshelf", 120, 8)
    add_product_to_category("living_room", "lr5", "Armchair", 250, 12)
    print('-' * 50)  # Horizontal line

    # Bedroom Products
    add_product_to_category("bedroom", "br1", "Bed Frame", 700, 20)
    add_product_to_category("bedroom", "br2", "Nightstand", 90, 30)
    add_product_to_category("bedroom", "br3", "Wardrobe", 500, 5)
    add_product_to_category("bedroom", "br4", "Dresser", 300, 10)
    add_product_to_category("bedroom", "br5", "Bedside Lamp", 40, 50)
    print('-' * 50)  # Horizontal line

    # Kitchen Products
    add_product_to_category("kitchen", "kt1", "Dining Set", 900, 7)
    add_product_to_category("kitchen", "kt2", "Refrigerator", 1200, 3)
    add_product_to_category("kitchen", "kt3", "Microwave Oven", 200, 20)
    add_product_to_category("kitchen", "kt4", "Kitchen Island", 600, 4)
    add_product_to_category("kitchen", "kt5", "Bar Stool", 75, 18)
    print('-' * 50)  # Horizontal line

    # Dining Room Products
    add_product_to_category("dining_room", "dr1", "Dining Table", 700, 5)
    add_product_to_category("dining_room", "dr2", "Dining Chair", 120, 30)
    add_product_to_category("dining_room", "dr3", "Buffet Table", 500, 4)
    add_product_to_category("dining_room", "dr4", "China Cabinet", 850, 3)
    add_product_to_category("dining_room", "dr5", "Table Runner", 25, 40)
    print('-' * 50)  # Horizontal line

    # Bathroom Products
    add_product_to_category("bathroom", "bt1", "Bathroom Vanity", 400, 8)
    add_product_to_category("bathroom", "bt2", "Shower Curtain", 20, 60)
    add_product_to_category("bathroom", "bt3", "Bathroom Mirror", 100, 15)
    add_product_to_category("bathroom", "bt4", "Storage Cabinet", 150, 6)
    add_product_to_category("bathroom", "bt5", "Towel Set", 35, 50)  
    print('-' * 50)  # Horizontal line
     # add_user('U001', 'Alice', 'alice@example.com')
    # add_user('U002', 'Sam', 'sam@gmail.com')
    # add_user('U003', 'Alex', 'alex@hotmail.com')
    # add a field to document "user ""
    # merge_field_user('U003', 'Alex', 'alex@hotmail.com')
    # filter products collection data
    # filter_products()
    # order_products()
    # print("\nProducts:")
    # get_products()
    # print("\nUsers:")
    # get_users()

    # Update data
    # update_product('P001', {'price': 1100.00})
    # update_user('U001', {'name': 'Alice Smith'})

    # Delete data
    # delete_product('P001')
    # delete_user('U001')
