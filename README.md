#Skeleton is a Python Flask app template for quick UI prototyping

Basic Flask application with Twitter Bootstrap and other Front end development utilities.

This project template is intended to do quick UI prototyping. Flask enables Less and Coffeescript
asset compilation through webassets and Twitter Bootstrap is included for fast frontend development.

To import YAML data, do `import YAML` on views.py and use like this:

    @app.route('/example')
    @templated()
    def example():
        with file('skeleton/data/example.yml', 'r') as stream:
            data = yaml.load(stream)
        return dict(examplelist=data)


##Contact

- Email: peter.hillerstrom@gmail.com
- Twitter: http://twitter.com/peterhil
- Homepage: http://composed.nu/

##License

Copyright (c) 2013 [Peter hillerström](https://github.com/peterhil)  
This software is licensed under the MIT License. See LICENSE for details.

##Credits

Skeleton uses the following libraries:

- ### [Twitter Bootstrap](https://github.com/twbs/bootstrap)

    Copyright 2012 Twitter, Inc.  
    Licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)

    Authors:  
    [Mark Otto](http://twitter.com/mdo) ([Github](http://github.com/markdotto))  
    [Jacob Thornton](http://twitter.com/fat) ([Github](http://github.com/fat))

- ### [Font Awesome](http://fortawesome.github.com/Font-Awesome)

    Version 2.0 of the Font Awesome font, CSS, and LESS files are  
    licensed under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/)
