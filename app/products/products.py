from flask import Blueprint, render_template

products_bp = Blueprint("products_bp", __name__, template_folder='templates', static_folder='static')

@products_bp.route('/')
def index():
    return render_template('products/index.html')

@products_bp.route('/single/<int:product_id>')
def view_product(product_id):
    return render_template('products/single.html')