from app.products import products_bp
from app.general import general_bp
from app.cart import cart_bp

def register_routes(app):
    app.register_blueprint(general_bp)
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(cart_bp, url_prefix="/cart")
