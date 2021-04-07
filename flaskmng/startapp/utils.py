from os.path import join

def create_app_init_py(app_name):
    def wrapper():
        with open(join(app_name, "__init__.py"), "w") as f:
            f.write("")
    return wrapper

