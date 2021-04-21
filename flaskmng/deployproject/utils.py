import os
def create_app_ini():
    with open("wsgi.py","w") as f:
        f.write(f"""\
[uwsgi]
wsgi-file = app.py
callable = app
socket = :8080
processes = 4
threads = 2
master = true
chmod-socket = 660
vacuum = true
die-on-term = true\
""")

def create_service_file(project_path,project_name,username,venv_name):
    def wrapper():
        with open(f"/etc/systemd/system/{project_name}.service","w") as f:
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

def create_nginx_file(project_path,prj_name,domain_name):
    def wrapper():
        try:
            os.mkdir("/etc/nginx/sites-available")
        except Exception as e:
            pass
        with open(f"/etc/nginx/sites-available/{prj_name}","w") as f:
            f.write(f"""\
server {{
    listen 80;
    server_name {domain_name} www.{domain_name};

    location / {{
        include proxy_params;
        proxy_pass http://unix:{project_path}/{prj_name}.sock;
    }}
}}
""")
    return wrapper