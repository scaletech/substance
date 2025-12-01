#!/usr/bin/env python3
import click


@click.group()
def cli():
    """Top-level command group for the CLI."""
    # You can put setup code here if needed (logging, config, etc.)
    pass


@cli.command()
@click.argument("name")
@click.option(
    "--greeting",
    "-g",
    default="Hello",
    show_default=True,
    help="Greeting to use.",
)
def greet(name: str, greeting: str):
    """Greet someone by NAME."""
    click.echo(f"{greeting}, {name}!")


@cli.command()
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable verbose output.",
)
def status(verbose: bool):
    """Show a simple status message."""
    if verbose:
        click.echo("Status: everything is running smoothly (verbose mode).")
    else:
        click.echo("Status: OK")


if __name__ == "__main__":
    cli()