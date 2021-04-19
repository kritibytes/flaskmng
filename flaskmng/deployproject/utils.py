def create_wsgi_py(project_name):
    def wrapper():
        with open("wsgi.py","w") as f:
            f.write(f"""\
from {project_name} import app

if __name__ == "__main__":
    app.run()\
""")
    return wrapper

def create_service_file(project_path,project_name,username,venv_name):
    def wrapper():
        with open(f"/etc/systemd/system/{project_name}.service") as f:
            f.write(f"""\
[Unit]
Description=Gunicorn instance to serve {project_name}
After=network.target

[Service]
User={username}
Group=www-data
WorkingDirectory={project_path}
Environment="PATH={project_path}/{venv_name}/bin"
ExecStart={project_path}/{venv_name}/bin/gunicorn --workers 3 --bind unix:{project_name}.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target\
""")
    return wrapper