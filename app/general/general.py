from flask import Blueprint, render_template
from app.products.model import Product

general_bp = Blueprint("general_bp", __name__, template_folder='templates', static_folder='static')

@general_bp.route('/')
def index():
    products = Product.query.all()
    return render_template('general/index.html', products=products)