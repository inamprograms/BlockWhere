from flask import Flask
from api import api_bp  # Import the Blueprint

app = Flask(__name__)

# Register the API Blueprint
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
