import click


@click.command()
@click.argument('name')
@click.option('--greeting', '-g', default='Hello2', help='')
def hello1(name, greeting):
    click.echo("{}, {}".format(greeting, name))


@click.command()
@click.argument('name')
@click.option('--greeting', '-g', default='Hello1', help='')
def hello2(name, greeting):
    click.echo("{}, {}".format(greeting, name))



if __name__ == "__main__":
    """
    This runs when you execute '$ python3 mypackage/mymodule.py
    '"""
    hello1()
