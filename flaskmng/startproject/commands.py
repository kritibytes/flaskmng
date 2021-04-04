import os
import click
from ..utils import MultiCommand, command_process_step, clear_screen, process_ok
from .utils import border
from python_script_manager.package import PSMReader


@click.group(cls=MultiCommand)
def startproject():
    pass


@startproject.command("startproject")
def startproject_command():
    processes = []
    process_ok(processes)

    # Install PSM
    command_process_step(
        "Installing PSM...", "pip install --upgrade python-script-manager")
    processes.append("Installed PSM")
    process_ok(processes)

    # Create psm.json
    command_process_step("Initializing PSM...",
                         'psm init --template="blank"')
    processes.append("Initialized PSM")
    process_ok(processes)
    
    # Create config field
    psm = PSMReader('psm.json')
    psm_config = psm.get_config()
    psm_config["APPS"] = []
    psm.set_config(psm_config)
    psm.write()
