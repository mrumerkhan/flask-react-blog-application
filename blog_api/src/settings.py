from pathlib import Path
import configparser
import os

BASE_DIR = Path(__file__).resolve().parent.parent

ENV = os.environ.setdefault("BLOG_ENV", "development")

CONFIG = configparser.ConfigParser()
CONFIG.read(BASE_DIR / "resources" / "{}.ini".format(ENV))

DEBUG = CONFIG.getboolean("DEFAULT", "DEBUG")

SQLALCHEMY_DATABASE_URI = CONFIG.get("DEFAULT", "SQLALCHEMY_DATABASE_URI")
