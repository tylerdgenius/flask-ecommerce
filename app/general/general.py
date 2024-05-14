from flask import Blueprint, render_template, request, session, jsonify
from app.products.model import Product

general_bp = Blueprint("general_bp", __name__, template_folder='templates', static_folder='static')

@general_bp.route('/')
def index():
    sort_by = request.args.get('sort_by', default='name', type=str)

    if sort_by == 'name':
        sorted_products = Product.query.order_by(Product.name).all()
    elif sort_by == 'price':
        sorted_products = Product.query.order_by(Product.price).all()
    elif sort_by == 'environmental_impact':
        sorted_products = Product.query.order_by(Product.environmental_impact).all()
    else:
        return jsonify({'error': 'Invalid sorting criteria'}), 400
    
    sorted_products_data = [{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'picture_url': product.picture_url,
        'price': product.price,
        'environmental_impact': product.environmental_impact,
        'is_in_cart': (True if ('cart' in session and product.id in session['cart']) else False)
    } for product in sorted_products]

    return render_template('general/index.html', products=sorted_products_data, default_sort_by=sort_by)