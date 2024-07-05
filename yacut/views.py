
import urllib

from flask import flash, redirect, render_template, request

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = get_unique_short_id()

    if URLMap.query.filter_by(short=custom_id).first() is not None:
        flash(
            'Предложенный вариант короткой ссылки уже существует.'
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


@app.route('/<short_url>', methods=['GET'])
def reroute_view(short_url):
    reroute = URLMap.query.filter_by(short=short_url).first_or_404()
    return redirect(reroute.original)
