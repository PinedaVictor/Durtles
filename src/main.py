# Main function

import typer
from count_folders import count_folders_dir
from rename import preview_rename
app = typer.Typer()


@app.command("count")
def handle_cp():
    """
     Count number of folders in a directory.
    """
    count_folders_dir()


@app.command("prename")
def handle_prename():
    preview_rename()


if __name__ == '__main__':
    app()