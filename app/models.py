from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    sites = db.relationship('Site', backref='owner', lazy=True)

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='waiting')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SiteForm(FlaskForm):
    url = StringField('Site URL', validators=[DataRequired()])
    submit = SubmitField('Add Site')
