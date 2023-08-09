from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "peanutbutter"
db.init_app(app)

class User(db.Model):
    """Users Model"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

