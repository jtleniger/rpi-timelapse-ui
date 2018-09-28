from flask_wtf import FlaskForm
from wtforms.fields.html5 import IntegerField
from wtforms.validators import NumberRange

class RunTimelapseForm(FlaskForm):
    count = IntegerField("Exposure Count", validators=[NumberRange(min=1)])
    duration = IntegerField("Shutter Speed (s)", validators=[NumberRange(min=1)])
    spacing = IntegerField("Interval (s)", validators=[NumberRange(min=0)])