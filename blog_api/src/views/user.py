from http import HTTPStatus

from flask import jsonify, request, views
from models import User, Token
from schemas import UserSchema
from utils import db

from utils.decorators import TokenAuthentication


class UserView(views.MethodView):
    """User View"""

    model = User
    schema_class = UserSchema

    def post(self, *args, **kwargs):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        if not email or not password:
            return (
                jsonify({"message": "Please provide email and password."}),
                HTTPStatus.BAD_REQUEST,
            )

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return (
                jsonify({"message": "User with that email already exists."}),
                HTTPStatus.CONFLICT,
            )

        new_user = User(email=email, first_name=first_name, last_name=last_name)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully."}), HTTPStatus.CREATED

    def get(self, *args, **kwargs):
        users = User.query.all()

        if not users:
            return jsonify({"message": "No users found"})

        output = []
        for user in users:
            user_data = {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "is_active": user.is_active,
                "date_joined": user.date_joined,
                "last_login": user.last_login,
            }
            output.append(user_data)

        return jsonify({"users": output}), HTTPStatus.OK


class LoginView(views.MethodView):
    """ "Login View"""

    def post(self, *args, **kwargs):
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return (
                jsonify({"message": "Please provide email and password."}),
                HTTPStatus.BAD_REQUEST,
            )

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return (
                jsonify({"message": "Invalid email or password."}),
                HTTPStatus.UNAUTHORIZED,
            )

        token = Token.query.filter_by(user_id=user.id).first()
        if not token:
            token = Token(user_id=user.id)
            db.session.add(token)
            db.session.commit()

        return (
            jsonify({"message": "Login successful.", "token": token.key}),
            HTTPStatus.CREATED,
        )


class LogoutView(views.MethodView):
    """Logout View"""

    decorators = [TokenAuthentication()]
    model = Token

    def delete(self, *args, **kwargs):
        self.model.query.filter_by(user_id=request.user.id).delete()
        db.session.commit()
        return (
            jsonify({"msg": "You are successfully Logged Out"}),
            HTTPStatus.NO_CONTENT,
        )
