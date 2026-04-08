import click


@click.command()
def main() -> None:
    """
    Main entry point for the PyBeli CLI.
    """
    click.echo("Welcome to PyBeli!")


if __name__ == "__main__":
    main()
