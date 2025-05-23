## Installation of Ninhursag for development

### 1. Checkout this repository from git

    git clone https://github.com/peterhil/ninhursag ninhursag-git
    cd ninhursag-git

All commands should be executed on project's root directory unless
otherwise noted.

### 2. Make sure a Python version greater than or equal to 3.8 is installed

Most Linux distributions come with Python already installed, if not
see the [Python 3 documentation](https://docs.python.org/3/using/index.html) for
instructions on how to install Python.

### 3. Install the system requirements

Install node and pnpm:

    sudo port install node
    sudo port install pnpm

If you are using a different operating system and package manager, replace 
the `sudo port` command with your system’s package manager – for example 
`pacman` or `apt-get`.

### 4. Install Python and dependencies

Install Python into virtualenv:

    python -m venv --prompt ninhursag-py310 venv/py310
    source ./venv/py310/bin/activate

Install Python dependencies with pip and pdm:

    pip install pdm
    pdm install

Pip should be install automatically with a virtualenv.

### 5. Install the node components

    pnpm install

### 6. Start the app

    source ./venv/py310/bin/activate
    pnpm start

Set Flask options using the `.env` file or set environment variables:

    source ./venv/py310/bin/activate
    cp docs/dot.env.example .env
    emacs .env  # Set the secret key at least
    FLASK_ENV=development DEBUG=true ASSETS_DEBUG=true flask run

Open the visualisation in a web browser:

    open http://localhost:5000/

###  7. Configuration

The application’s default settings can be found on `app/settings.py`.

These can be overridden by copying the defaut settings file to
`instance/settings.py`. Edit that file to suit your needs, and drop
unmodified values to prevent shadowing the default settings.

At minimum you should set `SECRET_KEY` to some unguessable and
randomish value. You might also want to set `SERVER_NAME` to match
your development server address (possibly with a port number).

To generate the secret key:

    python -c 'import secrets; print(secrets.token_hex())'

For a more fine detailed configuration, see the [list of built-in
settings](https://flask.palletsprojects.com/en/stable/config/#builtin-configuration-values)
on [Flask documentation](https://flask.palletsprojects.com/en/stable/).

Some of these settings are exported to front end from the route
`/config.json` at `app/frontend/views.py` and are available from
Javascript at `app.config` with the keys lower cased.

#### Nginx as a reverse proxy

On production and maybe even on development, you should set up Nginx
as a reverse proxy to your application or use some other
[Flask production deployment option](https://flask.palletsprojects.com/en/stable/tutorial/deploy/).

See [docs/nginx.md](docs/nginx.md) on how to do that.
