from flask import Blueprint, render_template, jsonify
from .model import Product

products_bp = Blueprint("products_bp", __name__, template_folder='templates', static_folder='static')

@products_bp.route('/')
def index():
    return render_template('products/index.html')

@products_bp.route('/single/<int:product_id>')
def view_product(product_id):
    return render_template('products/single.html')

@products_bp.route('/get_product_details/<int:product_id>')
def get_product_detail(product_id):
    # product = Product.query.filter_by(id=product_id).first()
    # if product is None:
    #     return 
    product = Product.query.get_or_404(product_id)

    description = product.description

    return jsonify({'description': description})