#
# Victor Pineda
# Description: List all folders in the Layers directory.

import os
import typer
from global_ import EDITING_DIR

app = typer.Typer()


@app.command("d")
def count_folders_dir(g: str = typer.Option("", help="SEE what it is")):
    """
     Count number of folders in a directory.
    """
    try:
        num_of_folders = len(os.listdir(EDITING_DIR))
        typer.secho(num_of_folders, fg=typer.colors.GREEN)
    except:
        if not os.path.isdir(EDITING_DIR):
            print("Directory does not exist")
        else:
            print("Error has occurred")


if __name__ == "__main__":
    app()
