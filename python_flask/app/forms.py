from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, length, Regexp
from python_flask.app.models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入密码')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    # username = StringField("用户名", validators=[DataRequired('请输入用户名')])
    username = StringField("用户名", validators=[length(min=2, max=8, message='用户名必须大于2位小于8位')])
    # email = StringField("邮箱", validators=[DataRequired(), Email('请输入邮箱')])
    email = StringField("邮箱", validators=[Regexp(regex=r"\w+@\w+\.\w+", message='邮箱格式错误'), Email()])
    # password = PasswordField("密码", validators=[DataRequired('请输入密码')])
    password = PasswordField("密码", validators=[length(min=2, max=8, message='密码必须大于2位小于8位')])
    password2 = PasswordField("重复密码", validators=[DataRequired('请输入密码'), EqualTo('password')])
    submit = SubmitField('注册')

    # 校验用户名是否重复
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户名重复了，请您重新换一个呗！')

    # 校验邮箱是否重复
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱重复了，请您重新换一个呗！')


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名！')])
    about_me = TextAreaField('关于我', validators=[length(min=0, max=140)])
    submit = SubmitField('提交')