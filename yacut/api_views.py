import re

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id

REGEX_ALPHANUMERIC = r'^[A-Za-z0-9]+$'


def check_required_field(api_data: dict, required_field: str):
    """Вызывает исключение если в запросе отсутствует обязательное поле."""
    if api_data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if required_field not in api_data:
        raise InvalidAPIUsage(
            f'"{required_field}" является обязательным полем!')


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json(silent=True)

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    custom_id = data.get('custom_id')
    if custom_id:
        print(f'Запрос с кастомным url: {custom_id}')
        if len(custom_id) > 16:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )

        if not re.fullmatch(REGEX_ALPHANUMERIC, custom_id):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if custom_id == 'example':
            print(URLMap.query.filter_by(short=custom_id).first())
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )
    else:
        custom_id = get_unique_short_id(0)

    urlmap = URLMap(
        original=data['url'],
        short=custom_id
    )
    db.session.add(urlmap)
    db.session.commit()

    return jsonify(urlmap.api_creation_to_dict(request)), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_link(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify(urlmap.api_redirection_to_dict()), 200
