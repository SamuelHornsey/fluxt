import typer
import importlib
import rich

from fluxt import __version__

cli = typer.Typer()


@cli.command()
def run(module_name, app='fluxt'):
    """ run fluxt app """
    module = importlib.import_module(module_name)
    fluxt = getattr(module, app)

    fluxt.run()


@cli.command()
def server():
    """ start fluxt server """
    pass


@cli.command()
def submit():
    """ submit job to fluxt server """
    pass


@cli.command()
def about():
    """ show info about fluxt """
    rich.print('\n'
               f'███████╗██╗     ██╗   ██╗██╗  ██╗████████╗\n'
               f'██╔════╝██║     ██║   ██║╚██╗██╔╝╚══██╔══╝\n'
               f'█████╗  ██║     ██║   ██║ ╚███╔╝    ██║   \n'
               f'██╔══╝  ██║     ██║   ██║ ██╔██╗    ██║   \n'
               f'██║     ███████╗╚██████╔╝██╔╝ ██╗   ██║   \n'
               f'╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   \n\n'
               f'version: {__version__}\n'
               f'license: MIT\n'
               f'source: https://github.com/SamuelHornsey/fluxt\n')
