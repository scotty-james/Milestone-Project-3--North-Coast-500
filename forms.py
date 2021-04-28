from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo

# All forms created using WTForms (https://flask-wtf.readthedocs.io/en/stable/quickstart.html)


# Sign Up Form


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

# Sign In Form


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# Add Review Form


class AddReviewForm(FlaskForm):
    category_name = SelectField('Route', choices=[('1', 'North Coast 500')])
    star_rating = SelectField('Rate Your Experience', choices=[(
        '5', '5 Star'), ('4', '4 Stars'), ('3', '3 Stars'), ('2', '2 Stars'), ('1', '1 Stars')])
    post_title = StringField('Give your review a title',
                             validators=[DataRequired()])
    post_description = TextAreaField(
        'Write about your experience', validators=[DataRequired()])
    image_url = StringField(
        'Post an image (paste in the url starting with https://)', validators=[DataRequired()])
    submit = SubmitField('Submit Review')

# Edit Review Form


class EditReviewForm(FlaskForm):
    category_name = SelectField('Route', choices=[('1', 'North Coast 500')])
    star_rating = SelectField('Rate Your Experience', choices=[(
        '5', '5 Star'), ('4', '4 Stars'), ('3', '3 Stars'), ('2', '2 Stars'), ('1', '1 Stars')])
    post_title = StringField('Give your review a title',
                             validators=[DataRequired()])
    post_description = TextAreaField(
        'Write about your experience', validators=[DataRequired()])
    image_url = StringField(
        'Post an image (past in the url)', validators=[DataRequired()])
    submit = SubmitField('Update Review')

# Delete Review Form


class DeleteForm(FlaskForm):
    post_title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Delete')
