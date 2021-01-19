# helloworld.py
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')

def hello(count=1, name='Kristof'):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        print('Hello %s!' % name)

if __name__ == '__main__':
    hello()