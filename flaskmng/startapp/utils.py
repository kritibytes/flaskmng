from os.path import join

def create_app_init_py(app_name):
    def wrapper():
        with open(join(app_name, "__init__.py"), "w") as f:
            f.write("")
    return wrapper

def create_models_py(app_name):
    def wrapper():
        with open(join(app_name,"models.py"),"w") as f:
            body_text = """\
from .. import db
            """
            f.write(body_text)
    return wrapper

def create_forms_py(app_name):
    def wrapper():
        with open(join(app_name,"forms.py"),"w") as f:
            body_text = """\
from flask_wtf import FlaskForm
            """
            f.write(body_text)
    return wrapper

def create_routes_py(prj_name,app_name):
    def wrapper():
        with open(join(prj_name,app_name,"routes.py"),"w") as f:
            body_text = f"""\
from flask import render_template, redirect, url_for, Blueprint

{app_name} = Blueprint('{app_name}', __name__, template_folder='templates')

@{app_name}.route('/')
def index():
    return "Hello!!!"
            """
            f.write(body_text)
    return wrapper