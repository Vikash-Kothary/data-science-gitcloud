from flask import Blueprint, current_app, jsonify
from flask_swagger import swagger as spec

from git_portfolio import __all__

swagger = Blueprint('swagger', __name__)

@swagger.route('/api-docs')
def swagger_spec():
	openapi = spec(current_app)
	openapi['swagger'] = '3.0.3'
	openapi['info']['version'] = __version__
	openapi['info']['title'] = __version__
	
	return jsonify(openapi)


@swagger.route('/swagger-ui')
def swagger_ui():
	return 'TODO'
