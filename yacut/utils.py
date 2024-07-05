from http import HTTPStatus
from random import choice

from flask import abort
from settings import CHAR_CHOICES, GENERATED_ID_LENGTH, MAX_GENERATION_ATTEMPTS

from .error_handlers import InvalidAPIUsage
from .models import URLMap


def get_unique_short_id(call_number=0):
    if call_number > MAX_GENERATION_ATTEMPTS:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    text = ''.join([choice(CHAR_CHOICES) for _ in range(GENERATED_ID_LENGTH)])
    if not URLMap.query.filter_by(short=text).first():
        return text
    return get_unique_short_id(call_number + 1)


def validate_api_data(data):
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
