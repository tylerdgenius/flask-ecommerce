from app.products.model import Product
import math

def get_products_by_ids(product_ids):

    if not product_ids:
        return []
    
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    return products

def get_cart_products(session):
    cart_contents = session.get('cart', [])
    products_in_cart = get_products_by_ids(cart_contents)
    cart_details = []
    unrounded_cost = 0

    for product in products_in_cart:
        unrounded_cost += product.price
        cart_details.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'picture_url': product.picture_url,
            'price': product.price,
            'environmental_impact': product.environmental_impact
        })


    total_cost = math.ceil(unrounded_cost)

    return cart_details, total_cost

    