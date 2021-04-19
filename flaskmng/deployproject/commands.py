from os.path import join
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
    take_input
)
from .utils import (
    remove_app,
    remove_app_imports
)

from ..__main__ import main

@main.command("deployproject")
def deployproject_command():
    pass