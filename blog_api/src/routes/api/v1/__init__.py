from flask import Blueprint

from routes.api.v1.blog import blog
from routes.api.v1.account import account

urlpatterns = [
    ("/account", account),
    ("/blog", blog),
]

v1 = Blueprint("v1", __name__)
for url_prefix, blueprint in urlpatterns:
    v1.register_blueprint(blueprint, url_prefix=url_prefix)
