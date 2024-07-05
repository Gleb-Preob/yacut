import urllib
from datetime import datetime

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(512), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(
        db.DateTime, index=True, default=datetime.utcnow
    )

    def api_creation_to_dict(self, request):
        return dict(
            url=self.original,
            short_link=urllib.parse.urljoin(request.url_root, self.short)
        )

    def api_redirection_to_dict(self):
        return dict(url=self.original)
