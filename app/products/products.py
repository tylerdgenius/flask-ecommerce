from flask import Blueprint, render_template, jsonify, url_for, redirect
from .model import Product

products_bp = Blueprint("products_bp", __name__, template_folder='templates', static_folder='static')

@products_bp.route('/')
def index():
    return redirect(url_for('general_bp.index'))

@products_bp.route('/single/<int:product_id>')
def view_product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('products/single.html', product=product)

@products_bp.route('/get_product_details/<int:product_id>', methods=['GET'])
def get_product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    description = product.description
    return jsonify({'description': description})

@products_bp.route("/sort_items/<string:sort_by>", methods=['GET'])
def sort_products(sort_by):
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
        'environmental_impact': product.environmental_impact
    } for product in sorted_products]

    return jsonify(sorted_products_data)