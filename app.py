from flask import Flask, request
from registry.vessel import vessel_bp
from registry.vessel_item import vessel_item_bp
from urllib.parse import urlparse
from urllib.parse import parse_qs

app = Flask(__name__)
app.register_blueprint(vessel_bp)
app.register_blueprint(vessel_item_bp)

if __name__ == '__main__':
    app.run(debug=True)
