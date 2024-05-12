from .sample_data import sample_data
from .products.model import Product
from .database import db

def is_products_table_empty():
    try:
        product_count = db.session.query(Product.id).count()
        return product_count == 0
    except Exception as e:
        print(f"Error checking product table: {e}")
        return False

def load_data():
        if is_products_table_empty():
            for data in sample_data:
                product = Product(
                    name=data['name'],
                    description=data['description'],
                    picture_url=data['picture_url'],
                    price=data['price'],
                    environmental_impact=data['environmental_impact']
                )
                
                db.session.add(product)

                db.session.commit()
                print("Data loaded successfully!")
        else:
            print("Products table is not empty. Skipping data insertion.")