import os
import click
from ..utils import MultiCommand, command_process_step

@click.group(cls=MultiCommand)
def startproject():
    pass

@startproject.command("startproject")
def startproject_command():
    command_process_step("Installing PSM...", "pip install --upgrade python-script-manager", "Installed PSM.")
