import os
import click
from ..utils import MultiCommand, command_process_step, clear_screen, process_ok, process_step, create_folder
from .utils import write_requirements
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

    # Creating requirements.txt
    process_step("Creating requirements.txt", write_requirements)
    processes.append("Created requirements.txt")
    process_ok(processes)

    # Installing requirements.txt
    command_process_step("Installing requirements.txt...",
                         'psm install')
    processes.append("Installed requirements.txt")
    process_ok(processes)

    # Creating main app folder
    process_step("Creating project folder...",
                        create_folder(psm.get_name()))
    processes.append("Created project folder")
    process_ok(processes)
