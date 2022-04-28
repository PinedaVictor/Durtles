# Main function
import typer
from count import count_folders_dir
import rename

app = typer.Typer()
app.add_typer(rename.app, name="rename")


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
