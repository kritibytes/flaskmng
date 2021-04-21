import os
import getpass
from python_script_manager.package import PSMReader
from ..utils import (
    command_process_step,
    process_ok,
    process_step,
    success_message,
    hl,
    take_input,
    detect_venv
)
from .utils import (
    create_app_ini
)
from ..__main__ import main

@main.command("deploysetup")
def deploysetup_command():
    psm = PSMReader()
    prj_name = psm.get_config().get('PROJECT_NAME', None)
    processes = []
    process_ok(processes)
    domain_name = take_input("Enter your domain name(without any subdomain): ")
    venv_name = detect_venv()
    project_path = os.getcwd()
    username = getpass.getuser()

    # Creating app.ini
    process_step(f"Creating {hl('app.ini')}...", create_app_ini)
    processes.append(f"Created {hl('app.ini')}")
    process_ok(processes)

    

    # Allowing Nginx
    command_process_step("Allowing nginx...", "ufw allow 'Nginx Full'")
    processes.append("Allowed nginx")
    process_ok(processes)

    # Show success message
    success_message(f"Successfully deployed {hl(prj_name)}")