from flask import Flask,render_template,redirect,url_for,flash,session
from forms import *
import os
from flask_login import LoginManager, login_user, current_user, logout_user
from models import *
# from flask_admin import Admin ,AdminIndexView
# from flask_admin.contrib.sqla import ModelView
from admin import  *
# from passlib.hash import pbkdf2_sha256


app = Flask(__name__)
app.secret_key=os.environ.get('SECRET')
app.config['SECRET_KEY']= 'mysecret'
# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
# admin = Admin(app, name='microblog', template_mode='bootstrap4')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/flaskAdmin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize login manager
login = LoginManager(app)
login.init_app(app)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
# =========================== admin =========================
adminView = Admin(app)
adminView.add_view(UserModelView(User, db.session))
# =========================== end ===========================




@app.route('/')
def hello():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)