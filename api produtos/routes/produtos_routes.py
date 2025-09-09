from flask import Blueprint, request
from controllers.carro_controllers import create_carro

produtos_routes = Blueprint('produtos_routes', __name__)

@produtos_routes.route('/produtos', methods=['POST'])
def produtos_post():
    produtos_data = request.json
    return create_produtos(request.json)
