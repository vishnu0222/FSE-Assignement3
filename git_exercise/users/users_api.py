from flask import Flask, Blueprint, abort, jsonify, request
from git_exercise.users.users_gateway import UsersGateway
from git_exercise.users.user import User

# Initialize Flask app
app = Flask(__name__)

# Initialize UsersGateway
gateway = UsersGateway()

# Define Blueprint API
def users_api(users_gateway: UsersGateway) -> Blueprint:
    api = Blueprint("users_api", __name__)

    @api.route("/users", methods=["GET"])
    def list_all():
        return jsonify([user.to_dict() for user in users_gateway.list()])

    @api.route("/users/<int:user_id>", methods=["GET"])
    def find(user_id: int):
        user = users_gateway.find(user_id)
        if user is None:
            abort(404)
        return jsonify(user.to_dict())

    @api.route("/users", methods=["POST"])
    def create_user():
        data = request.json
        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "Missing 'name' or 'email'"}), 400

        new_user = User(id=len(users_gateway.users) + 1, name=data["name"], email=data["email"])
        users_gateway.users.append(new_user)
        return jsonify(new_user.to_dict()), 201

    @api.route("/users/<int:user_id>", methods=["PUT"])
    def update_user(user_id):
        user = users_gateway.find(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        data = request.json
        if "name" in data:
            user.name = data["name"]
        if "email" in data:
            user.email = data["email"]

        return jsonify(user.to_dict()), 200

    return api

# Register the Blueprint
app.register_blueprint(users_api(gateway))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
