import click
from get_subtitle import search_subtitle

@click.group()
def cli():
    """A simple CLI app with Click."""
    pass

@cli.command()
@click.argument('movie')
def get(movie):
    results = search_subtitle(movie)

    if not results:
        click.echo("No results found.")
        return
    click.echo("Available websites:")
    for title, url, downloads, languages in results:
        print(f"Title: {title};\nURL: {url};\nDownloads: {downloads}\nLanguages: {languages}")
        print('--------------------------')

if __name__ == '__main__':
    cli()
