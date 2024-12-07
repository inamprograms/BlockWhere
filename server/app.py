from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def wellcome():
    return "<center><h1> Wellcome to BlockWhere Technologies <h1></center>"

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error' : 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error' : 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')