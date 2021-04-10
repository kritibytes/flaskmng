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
    in_virtualenv,
    success_message,
    make_compatible,
    hl,
    take_input
)
from .utils import (
    remove_app
)


@click.group(cls=MultiCommand)
def removeapp():
    pass


@removeapp.command("removeapp")
def removeapp_command():
    if not in_virtualenv():
        raise Exception("You must be in virtual environment to run")
    
    psm = PSMReader()
    prj_name = psm.get_config().get('PROJECT_NAME', None)
    app_list = psm.get_config().get('APPS', None)
    processes = []
    process_ok(processes)

    # Taking app name to remove
    app_name = take_input("Enter name of app to remove:")

    # Removing app folder
    if not prj_name :
        raise Exception("You deleted your project name from psm.json file. Please add it.")
    if not app_name in app_list:
        raise Exception("Your app name is not in app list")
    try :
        process_step(f"Removing {hl(join(prj_name, app_name))} folder...",
                    remove_app(join(prj_name, app_name)))
        processes.append(f"Removed {hl(join(prj_name, app_name))} folder")
        process_ok(processes)
    except Exception as e:
        print("❌ "+str(e))

    # Removing app name from psm.json
    psm_config = psm.get_config()
    psm_config['APPS'].remove(app_name)
    psm.set_config(psm_config)
    psm.write()

    # Output success message
    success_message(f"Successfully removed {hl(app_name)}")
    info_message(f"Use {hl('psm run')} to run your application")
