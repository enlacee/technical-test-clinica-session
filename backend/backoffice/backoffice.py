from flask import Blueprint

backoffice_bp = Blueprint('backoffice', __name__)

@backoffice_bp.route('/')
def backoffice():
    return "<p>Hello, Worldx1</p>"