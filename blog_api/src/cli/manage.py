from getpass import getpass

from flask import Blueprint

from models import User
from schemas import UserSchema
from utils import db

manage = Blueprint("manage", __name__)


@manage.cli.command("createuser")
def createuser():
    """Create a user for the application."""
    email = input("Email: ")
    if User.query.filter_by(email=email).first():
        raise ValueError("User with this email already exists.")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    password = getpass("Password: ")
    confirm_password = getpass("Confirm password: ")
    if password != confirm_password:
        raise ValueError("Both the passwords should match.")
    data = {"email": email, "first_name": first_name, "last_name": last_name}
    schema = UserSchema()
    user = schema.load(data)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
