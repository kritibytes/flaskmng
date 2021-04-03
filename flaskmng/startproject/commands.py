import os
import click
from ..utils import MultiCommand

@click.group(cls=MultiCommand)
def startproject():
    pass

@startproject.command("startproject")
def startproject_command():
    print("Installing PSM...")
    print(">> pip install --upgrade python-script-manager")
    os.system("pip install --upgrade python-script-manager")
    print("Installed PSM.")
