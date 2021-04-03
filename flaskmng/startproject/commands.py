import os
import click
from ..utils import MultiCommand, command_process_step
from .utils import border
from python_script_manager.package import PSMReader

@click.group(cls=MultiCommand)
def startproject():
    pass

@startproject.command("startproject")
def startproject_command():
    # Installing PSM
    command_process_step("Installing PSM...", "pip install --upgrade python-script-manager", "Installed PSM.")
    
    border()
    # Create psm.json
    command_process_step("Initializing PSM...",'psm init --template="blank"',"Initialized PSM.")

    border()
    # Create config field
    psm = PSMReader('psm.json')
    psm_config = psm.get_config()
    psm_config["APPS"] = []
    psm.set_config(psm_config)
    psm.write()