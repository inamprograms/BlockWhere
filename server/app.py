from flask import Flask, jsonify
from flask_cors import CORS
from api.news_routes import news_routes

app = Flask(__name__)
CORS(app)

# Register the API Blueprint
app.register_blueprint(news_routes, url_prefix='/api')

# Welcome Route
@app.route('/')
def welcome():
    return "<center><h1>Welcome to BlockWhere Technologies</h1></center>"

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')