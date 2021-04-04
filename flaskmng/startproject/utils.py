def write_requirements():
    with open("requirements.txt", "w") as f:
        reqs_text = '''\
alembic
astroid
bcrypt
blinker
cffi
click
colorama
dnspython
email-validator
Flask
Flask-Bcrypt
Flask-Login
Flask-Mail
Flask-Migrate
Flask-SQLAlchemy
Flask-WTF
idna
isort
itsdangerous
Jinja2
lazy-object-proxy
Mako
MarkupSafe
mccabe
Pillow
pycparser
pylint
python-dateutil
python-editor
six
SQLAlchemy
toml
Werkzeug
wrapt
WTForms
wheel
'''
        f.write(reqs_text)


def create_gitignore():
    with open('.gitignore', 'w') as f:
        ignore_text = """\
venv
**/__pycache__
site.db
migrations/versions/**/*
"""
        f.write(ignore_text)

def create_app_py(name):
    def wrapper():
        with open('app.py','w') as f:
            app_py_text = f"""\
from {name} import app

if __name__=='__main__':
    app.run(debug=True)            
"""
            f.write(app_py_text)
    return wrapper