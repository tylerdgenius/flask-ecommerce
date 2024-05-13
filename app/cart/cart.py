from flask import Blueprint, jsonify, session, render_template
from app.utils import get_products_by_ids

cart_bp = Blueprint("cart_bp", __name__, template_folder='templates', static_folder='static')

@cart_bp.route('/')
def index():
    return render_template('cart/index.html')

@cart_bp.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []

    if product_id in session['cart']:
        return jsonify({"message": "Item already in cart"}), 500

    session['cart'].append(product_id)
    return jsonify({'message': 'Item added to cart'})

@cart_bp.route('/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    
    if 'cart' not in session:
        session['cart'] = []
    print(session['cart'])
    if product_id in session['cart']:
        session['cart'].remove(product_id)
        return jsonify({'message': f'Item {product_id} removed from cart'})
    else:
        return jsonify({'message': f'Item {product_id} not found in cart'}), 404

@cart_bp.route('/contents')
def get_cart_contents():
    cart_contents = session.get('cart', [])
    products_in_cart = get_products_by_ids(cart_contents)
    cart_details = []

    for product in products_in_cart:
        cart_details.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'picture_url': product.picture_url,
            'price': product.price,
            'environmental_impact': product.environmental_impact
        })

    return jsonify(cart_details)