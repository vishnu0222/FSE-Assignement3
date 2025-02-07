from flask import Flask

def test_client(blueprint):
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    return app.test_client()
