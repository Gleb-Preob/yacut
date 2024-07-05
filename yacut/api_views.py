import re
from http import HTTPStatus

from flask import jsonify, request
from settings import MAX_SHORT_ID_LENGTH, REGEX_ALPHANUMERIC

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id, validate_api_data


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json(silent=True)

    validate_api_data(data)

    custom_id = data.get('custom_id')
    if custom_id:
        if len(custom_id) > MAX_SHORT_ID_LENGTH:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )

        if not re.fullmatch(REGEX_ALPHANUMERIC, custom_id):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )
    else:
        custom_id = get_unique_short_id()

    urlmap = URLMap(
        original=data['url'],
        short=custom_id
    )
    db.session.add(urlmap)
    db.session.commit()

    return jsonify(urlmap.api_creation_to_dict(request)), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_link(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify(urlmap.api_redirection_to_dict()), HTTPStatus.OK
