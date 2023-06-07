from models import Blog
from utils import ma


class BlogSchema(ma.SQLAlchemyAutoSchema):
    """Blog Schema"""

    class Meta:
        model = Blog
        load_instance = True
        exclude = ["user_id"]
