import click
import os
from sys import platform
import time
import pyfiglet

class MultiCommand(click.Group):
    def command(self, *args, **kwargs):
        """Behaves the same as `click.Group.command()` except if passed
        a list of names, all after the first will be aliases for the first.
        """
        def decorator(f):
            if isinstance(args[0], list):
                _args = [args[0][0]] + list(args[1:])
                for alias in args[0][1:]:
                    cmd = super(MultiCommand, self).command(
                        alias, *args[1:], **kwargs)(f)
                    cmd.short_help = "Alias for '{}'".format(_args[0])
            else:
                _args = args
            cmd = super(MultiCommand, self).command(
                *_args, **kwargs)(f)
            return cmd
        return decorator


def command_process_step(start_text, command):
    print("⌛ "+start_text+"\n")
    print(f">> {command}\n")
    os.system(command)

def clear_screen():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

def process_ok(finished_process):
    clear_screen()
    text = pyfiglet.figlet_format("flaskmng", font = "slant"  )
    print(text)
    for i in finished_process:
        print("✔ "+i)