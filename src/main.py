# Main function

import typer


def main(arg: str = typer.Argument(...), script: str = typer.Option("", help="EH")):
    print(f"Main Function{arg}")


if __name__ == '__main__':
    typer.run(main)
