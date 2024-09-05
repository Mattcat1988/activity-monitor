from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SiteForm(FlaskForm):
    url = StringField('Site URL', validators=[DataRequired()])
    submit = SubmitField('Add Site')