from app.products.model import Product

def get_products_by_ids(product_ids):
    if not product_ids:
        return []
    
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    return products