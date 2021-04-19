from os.path import join
import os
import getpass
import click
from python_script_manager.package import PSMReader
from ..utils import (
    MultiCommand,
    command_process_step,
    info_message,
    process_ok,
    process_step,
    create_folder,
    success_message,
    make_compatible,
    hl,
    take_input,
    detect_venv
)
from .utils import (
    create_wsgi_py,
    create_service_file
)

from ..__main__ import main


@main.command("deployproject")
def deployproject_command():
    psm = PSMReader()
    prj_name = psm.get_config().get('PROJECT_NAME', None)
    processes = []
    process_ok(processes)

    # Creating wsgi.py
    process_step(f"Creating {hl('wsgi.py')}...", create_wsgi_py(prj_name))
    processes.append(f"Created {hl('wsgi.py')}")
    process_ok(processes)

    # Creating service file
    venv_name = detect_venv()
    project_path = os.getcwd()
    username = getpass.getuser()
    process_step(f"Creating {hl(f'/etc/systemd/system/{prj_name}.service')}...",
                 create_service_file(project_path, prj_name, username, venv_name))
    processes.append(
        f"Created {hl(f'/etc/systemd/system/{prj_name}.service')}")
    process_ok(processes)
