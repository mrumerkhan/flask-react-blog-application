"""Web Server Gateway Interface"""

from flask import Flask

from cli.manage import manage
from routes import urlpatterns
from utils import db, ma
import settings


def get_wsgi_application():
    app = Flask(__name__)
    app.config.update(
        DEBUG=settings.DEBUG,
        ENV=settings.ENV,
        SQLALCHEMY_DATABASE_URI=settings.SQLALCHEMY_DATABASE_URI
    )
    db.init_app(app)

    ma.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(manage)
    for url_prefix, blueprint in urlpatterns:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
    return app


application = get_wsgi_application()

if __name__ == "__main__":
    application.run()
