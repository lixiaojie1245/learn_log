import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--verbose', is_flag=True, help='Enables verbose mode.')
def hello(count, name, verbose):

    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")
    if verbose:
        click.echo(f'Verbose mode is enabled for {name}.')
    else:
        click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()
