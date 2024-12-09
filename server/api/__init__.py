from flask import Blueprint
#from get_response import generate_response  # Use relative import

api_bp = Blueprint('api', __name__)

@api_bp.route('/generate', methods=['POST'])
def api_generate():
    # Example usage of the generate_response function
    query = "Sample query"
    return generate_response(query)
