import sys
import click

from .startproject import startproject

commands = [
    startproject
]


main = click.CommandCollection(sources=commands)

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("flaskmng")
    main()