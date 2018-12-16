from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email,ValidationError
from blog.models import Candidate

class AddCandidateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    position = StringField('Position', validators=[DataRequired()])
    plan_id = SelectField('Plan requirement', validators=[DataRequired()],coerce=int)
    submit = SubmitField('Save')

    def validate_email(self, email):
        candidate = Candidate.query.filter_by(email=email.data).first()
        if candidate:
            raise ValidationError('That email is taken. Please choose a different one.')


   
class EditCandidateForm(FlaskForm):
    id =  IntegerField('id')
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    position = StringField('Position', validators=[DataRequired()])
    plan_id = SelectField('Plan requirement', validators=[DataRequired()],coerce=int)
    submit = SubmitField('Save')

    def validate_email(self, email):
        candidate = Candidate.query.filter_by(email=email.data).first()
        if candidate and candidate.id != self.id.data:
            raise ValidationError('That email is taken. Please choose a different one.')

 

