# Main function
import typer
from count import count_folders_dir
from rename import preview_rename

app = typer.Typer()


@app.command("rename")
def handle_rename(op: str = typer.Option("su")):
    # TODO: Define whether directory will be user input or defined globally
    """
    Renaming files within in a directory.
    """
    if(op == "p"):
        preview_rename()


@app.command("count")
def handle_count():
    """
     Count number of folders in a directory.
    """
    count_folders_dir()


def main():
    """
    Directory utilities that automate time-consuming tasks.
    """


if __name__ == '__main__':
    app()
