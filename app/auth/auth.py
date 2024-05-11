from flask import Blueprint, render_template

auth_bp = Blueprint("auth_bp", __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/register')
def register():
    return render_template('auth/signup.html')

@auth_bp.route('/forgot-password')
def forgot_password():
    return render_template('auth/forgot-password.html')