from flask_admin import Admin ,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from wtforms.validators import InputRequired, Required,ValidationError
from flask_admin.model import typefmt
from datetime import datetime
from flask_admin.menu import MenuLink

class UserModelView(ModelView):
    pass
