from flask import Flask

from .extensions import mongo

def create_app():
    app = Flask(__name__)
    
    app.config['MONGO_URI'] = "mongodb+srv://admin:adminpass@cluster0.v8b4u.mongodb.net/mydb?retryWrites=true&w=majority"
    mongo.init_app(app)

    from .main.routes import main
    app.register_blueprint(main)

    return app