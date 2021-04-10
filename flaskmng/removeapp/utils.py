import shutil

def remove_app(app_folder):
    def wrapper():
        shutil.rmtree(app_folder)
    return wrapper