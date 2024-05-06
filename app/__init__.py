from flask import Flask
from flask_restful import Api
from app.models import Design


# initiate
def create_app():
    app = Flask(__name__)

    api = Api(app)
    api.add_resource(Design, '/design', '/design/<int:id>')
    return app
