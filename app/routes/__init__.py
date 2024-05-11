from app.products import products_bp
from app.auth import auth_bp
from app.general import general_bp

def register_routes(app):
    app.register_blueprint(general_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(products_bp, url_prefix="/products")
