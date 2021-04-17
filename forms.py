from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class AddReviewForm(FlaskForm):
    category_name = StringField('Category', validators=[DataRequired()])
    post_title = StringField('Title', validators=[DataRequired()])
    post_description = TextAreaField('Review', validators=[DataRequired()])
    image_url = StringField('Image Url', validators=[DataRequired()])
    submit = SubmitField('Add Review')


class EditReviewForm(FlaskForm):
    category_name = StringField('Category', validators=[DataRequired()])
    post_title = StringField('Title', validators=[DataRequired()])
    post_description = TextAreaField('Review', validators=[DataRequired()])
    image_url = StringField('Image Url', validators=[DataRequired()])
    submit = SubmitField('Update Review')