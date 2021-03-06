from flask_wtf import Form as FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,SelectField
from wtforms.validators import Required,Length,Email,Regexp
from wtforms import ValidationError

class NameForm(FlaskForm):
    name = StringField("What is your name?",validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name',validators=[Length(1,64)])
    location = StringField('Location',validators=[Length(1,64)])
    about_me = TextAreaField("About me")
    submit=SubmitField("Submit")


class EditProfileAdminForm(FlaskForm):
    email = StringField("Email",validators = [Required(),Length(1,64),Email()])
    username = StringField("Username",validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames must only letters numbers dots or underscores')])
    confirmed = BooleanField("Confirmed")
    role = SelectField("Role",coerce=int)
    name = StringField("Real name",validators=[Required(),Length(1,64)])
    location = StringField("Location",validators=[Required(),Length(1,64)])
    about_me = TextAreaField("About me")
    submit = SubmitField("Submit")

    def __init__(self,user,*args,**kwargs):
        super(EditProfileAdminForm,self).__init__(*args,**kwargs)
        self.role.choices = [(role.id,role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user


    def validate_email(self,field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered")

    def validate_username(self,field):
        if field.data != self.user.username and User.query.fileter_by(username=field.data).first():
            raise ValidationError("Useraname already in use.")

class PostForm(FlaskForm):
    """
    This is the post form
    """
    # body = PageDownField("Whats on your mind",validators = [Required()])
    body = StringField("Whats on your mind",validators = [Required()])
    submit = SubmitField("Submit")

class CommentForm(FlaskForm):
    body = StringField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')


