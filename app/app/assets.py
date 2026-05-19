#!/usr/bin/env python

from flask_assets import Environment


def init_app(app):
    webassets = Environment(app)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
