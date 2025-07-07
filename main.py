import click
from get_subtitle import search_subtitle
from InquirerPy import inquirer

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
    choices = []
    for title, url, downloads, languages in results:
        choice = f"Title: {title};\nURL: {url};\nDownloads: {downloads}\nLanguages: {languages}"
        choices.append(choice)
    
    selection = inquirer.select(
        message="Select a subtitle result:",
        default=choices[0],
        choices=choices,
        pointer='=>',
        instruction='Use arrow keys to navigate and Enter to select.',
    ).execute()

    click.secho(f"You selected: {selection}", fg="green")

if __name__ == '__main__':
    cli()
