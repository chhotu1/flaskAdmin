from flask import Flask
import datetime
from sqlalchemy import DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import UserMixin
import enum

class UserRole(enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskAdmin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
class User(db.Model,UserMixin):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50))
	password = db.Column(db.String(200))
	is_authenticated = db.Column(db.Boolean, default=False)
	created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	def is_active(self):
		return True
	def get_id(self):
		return self.id
	def is_anonymous(self):
		return True
	def is_authenticated(self):
		return self.is_authenticated

	def __repr__(self):
		return self.name

class Contact(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))
	message = db.Column(db.String(100))
	mobile = db.Column(db.String(12))

	def __repr__(self):
		return self.name

if __name__ == '__main__':
    manager.run()