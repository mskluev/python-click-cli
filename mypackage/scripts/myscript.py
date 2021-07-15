import click


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.echo('Initialized the database')


@cli.command()
def dropdb():
    click.echo('Dropped the database')


@cli.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


# https://github.com/GreyNoise-Intelligence/pygreynoise/blob/master/src/greynoise/cli/helper.py
@cli.command()
def echo():
    input_file = click.open_file("-")
    input = input_file.readline()
    click.echo(input)


if __name__ == "__main__":
    cli()
