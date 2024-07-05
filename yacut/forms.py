from flask_wtf import FlaskForm
from settings import MAX_ORIGINAL_ID_LENGTH, MAX_SHORT_ID_LENGTH
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional
from wtforms_validators import AlphaNumeric


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, MAX_ORIGINAL_ID_LENGTH, message=(
                f'Превышена допустимая длина ссылки: {MAX_ORIGINAL_ID_LENGTH}')
            )
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, MAX_SHORT_ID_LENGTH, message=(
                f'Превышена допустимая длина ссылки: {MAX_SHORT_ID_LENGTH}')
            ),
            AlphaNumeric(message='Допускаются только латинские буквы и цифры'),
            Optional()]
    )
    submit = SubmitField('Создать')
