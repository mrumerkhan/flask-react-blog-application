from flask import Blueprint

from views.user import UserView, LoginView,LogoutView

account = Blueprint("account", __name__)
account.add_url_rule("/user", view_func=UserView.as_view("user"), methods=["POST"])
account.add_url_rule("/getuser", view_func=UserView.as_view("getuser"), methods=["GET"])
account.add_url_rule("/login", view_func=LoginView.as_view("login"), methods=["POST"])
account.add_url_rule("/logout", view_func=LogoutView.as_view("logout"), methods=["DELETE"])

