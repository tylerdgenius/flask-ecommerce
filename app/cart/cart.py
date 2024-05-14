from flask import Blueprint, jsonify, session, render_template, request
from app.utils import get_products_by_ids, get_cart_products

cart_bp = Blueprint("cart_bp", __name__, template_folder='templates', static_folder='static')


@cart_bp.route('/')
def index():
    count = 0
    if 'cart' in session:
        count = len(session['cart'])

    cart_details, total_cost = get_cart_products(session=session)

    print(cart_details, total_cost)

    return render_template('cart/index.html', count=count, products=cart_details)

@cart_bp.route('/process_payment', methods=['POST'])
def process_payment():
    form_data = request.get_json()
    credit_card = form_data.get('credit_card', '').replace('-', '').replace(' ', '')
    name = form_data.get('name', '')
    expiration = form_data.get('expiration', '')
    cvv = form_data.get('cvv', '')

    if not (credit_card.isdigit() and len(credit_card) == 16):
        return jsonify({'error': 'Invalid credit card number'}), 400

    if not name.strip():
        return jsonify({'error': 'Please enter your name'}), 400

    if not expiration.strip():
        return jsonify({'error': 'Please enter the expiration date'}), 400

    if not (cvv.isdigit() and (len(cvv) == 3 or len(cvv) == 4)):
        return jsonify({'error': 'Invalid CVV'}), 400

    return jsonify({'message': 'Checkout successful'})


@cart_bp.route("/checkout")
def checkout():
    cart_details, total_cost = get_cart_products(session=session)

    return render_template('cart/checkout.html', products=cart_details, total=total_cost)

@cart_bp.route('/clear', methods=['POST'])
def clear_cart():
    session['cart'] = []
    return jsonify({"message": "Cleared all items in cart"})

@cart_bp.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []

    if product_id in session['cart']:
        return jsonify({"message": "Item already in cart"}), 500
    
    session['cart'].append(product_id)
    session.modified = True
    print(session['cart'])
    return jsonify({'message': 'Item added to cart'})

@cart_bp.route('/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    print(session['cart'], product_id)
    if product_id in session['cart']:
        session['cart'].remove(product_id)
        session.modified = True
        return jsonify({'message': f'Item {product_id} removed from cart'})
    else:
        return jsonify({'message': f'Item {product_id} not found in cart'}), 404

@cart_bp.route('/contents')
def get_cart_contents():
    cart_details = get_cart_products(session=session)

    return jsonify(cart_details)