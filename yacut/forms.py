from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional
from wtforms_validators import AlphaNumeric


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 512, message='Превышена допустимая длина ссылки: 512')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16, message='Превышена допустимая длина ссылки: 16'),
            AlphaNumeric(message='Допускаются только латинские буквы и цифры'),
            Optional()]
    )
    submit = SubmitField('Создать')
