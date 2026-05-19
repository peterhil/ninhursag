#!/usr/bin/env python

from werkzeug.middleware.proxy_fix import ProxyFix

from . import factory
from . import log


def create_app(settings_override=None):
    """Returns the application instance"""
    app = factory.create_app(__name__, settings_override)

    # Init logging
    log.init_app(app)

    return app


# http://www.onurguzel.com/how-to-run-flask-applications-with-nginx-using-gunicorn/
app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    app.run()
