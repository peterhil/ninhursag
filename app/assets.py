#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.assets import Environment, Bundle


css_application = Bundle(
    'style/main.less',
    filters='less,autoprefixer',
    debug=False,
    output='gen/app.css'
)

css_foundation = Bundle(
    'vendor/foundation/css/normalize.css',
    'vendor/foundation/css/foundation.css',
    # filters='scss',
    output='gen/foundation.css'
)

css_all = Bundle(
    'vendor/angular-growl-v2/build/angular-growl-foundation.css',
    css_foundation,
    css_application,
    filters='cssmin',
    output='gen/app.min.css'
)

js_vendor = Bundle(
    'vendor/jquery/dist/jquery.js',
    'vendor/angular/angular.js',
    'vendor/angular-animate/angular-animate.js',
    'vendor/angular-aria/angular-aria.js',
    'vendor/angular-cookies/angular-cookies.js',
    'vendor/angular-messages/angular-messages.js',
    'vendor/angular-resource/angular-resource.js',
    'vendor/angular-route/angular-route.js',
    'vendor/angular-sanitize/angular-sanitize.js',
    'vendor/angular-touch/angular-touch.js',
    'vendor/angular-growl-v2/build/angular-growl.js',
    'vendor/lodash/dist/lodash.js',
    'vendor/Papa-Parse/papaparse.js',
    # 'vendor/modernizr/dist/modernizr-build.js', # TODO Customize this
    'vendor/foundation/js/foundation/foundation.js',
    'vendor/foundation/js/foundation/foundation.topbar.js',
    filters='uglifyjs',
    output='gen/vendor.min.js'
)

js_ie = Bundle(
    'vendor/es5-shim/es5-shim.js',
    filters='uglifyjs',
    output='gen/ie.min.js'
)

js_main = Bundle(
    Bundle(
        'coffee/production-chart.coffee',
        'script/app.coffee',
        'script/service/config.coffee',
        'script/controller/listing.coffee',
        'script/controller/mineral-ctrl.coffee',
        'script/directive/chart.coffee',
        filters='coffeescript',
        output='gen/app.js'
    ),
    filters='uglifyjs',
    output='gen/app.min.js'
)


def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.register('js_vendor', js_vendor)
    webassets.register('js_ie', js_ie)
    webassets.register('js_main', js_main)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
