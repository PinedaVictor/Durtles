# Main function
import typer
import count
from rename import preview_rename

app = typer.Typer()
app.add_typer(count.app, name="count")


@app.command("rename")
def handle_rename(op: str = typer.Option("su")):
    # TODO: Define whether directory will be user input or defined globally
    """
    Renaming files within in a directory.
    """
    if(op == "p"):
        preview_rename()


def main():
    """
    Directory utilities that automate time-consuming tasks.
    """


if __name__ == '__main__':
    app()
