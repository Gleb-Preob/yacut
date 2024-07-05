import string
import urllib
from random import choice

from flask import abort, flash, redirect, render_template, request

from . import app, db
from .forms import URLMapForm
from .models import URLMap

CHAR_CHOICES = string.ascii_lowercase + string.digits + string.ascii_uppercase


def get_unique_short_id(call_number):
    if call_number > 1000:
        abort(500)
    text = ''.join([choice(CHAR_CHOICES) for _ in range(6)])
    if not URLMap.query.filter_by(short=text).first():
        return text
    else:
        return get_unique_short_id(call_number+1)


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():

        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id(0)

        if URLMap.query.filter_by(short=custom_id).first() is not None:
            flash(
                f'Предложенный вариант короткой ссылки уже существует.'
            )
            return render_template('index.html', form=form)

        urlmap = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(urlmap)
        db.session.commit()
        return render_template(
            'index.html',
            form=form,
            new_link=urllib.parse.urljoin(request.url_root, urlmap.short)
        )

    return render_template('index.html', form=form)


@app.route('/<short_url>', methods=['GET'])
def reroute_view(short_url):
    reroute = URLMap.query.filter_by(short=short_url).first_or_404()
    return redirect(reroute.original)
