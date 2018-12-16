from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email,ValidationError
from blog.models import Plan
from wtforms.fields.html5 import DateField



class AddPlanForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=20)])
    date_start = DateField('Date start', validators=[DataRequired()])
    date_end = DateField('Date end', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_title(self, title):
        plan = Plan.query.filter_by(title=title.data).first()
        if plan:
            raise ValidationError('That title is taken. Please choose a different one.')


class EditPlanForm(FlaskForm):
    id =  IntegerField('id')
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=20)])
    date_start = StringField('Date start', validators=[DataRequired()])
    date_end = StringField('Date end', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_email(self, title):
        plan = Plan.query.filter_by(title=title.data).first()
        if plan and plan.id != self.id.data:
            raise ValidationError('That title is taken. Please choose a different one.')






