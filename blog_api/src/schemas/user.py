from models.user import User

from utils import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        load_only = ["password"]
