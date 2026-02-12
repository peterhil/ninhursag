#!/usr/bin/env python

from flask_assets import Environment, Bundle


css_pico = Bundle(
    'vendor/@picocss/pico/scss/pico.fluid.classless.scss',
    debug=False,
    filters=[
        'scss',
        'cssmin'
    ],
    output='gen/pico.css'
)

css_app = Bundle(
    'style/app.scss',
    debug=False,
    filters=[
        'scss',
        'cssmin'
    ],
    output='gen/app.css'
)

def init_app(app):
    webassets = Environment(app)
    webassets.register('css_pico', css_pico)
    webassets.register('css_app', css_app)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
