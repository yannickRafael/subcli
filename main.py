import click
from get_subtitle import search_subtitle_options, get_subtitle
from InquirerPy import inquirer

@click.group()
def cli():
    """A simple CLI app with Click."""
    pass

@cli.command()
@click.argument('movie')
def get(movie):
    results = search_subtitle_options(movie)

    if not results:
        click.echo("No results found.")
        return
    click.echo("Available websites:")
    titles = list(results.keys())
    
    selection = inquirer.select(
        message="Select a subtitle result:",
        default=titles[0],
        choices=titles,
        pointer='=>',
        instruction='Use arrow keys to navigate and Enter to select.',
    ).execute()

    url = results[selection][0]
    subtitles = get_subtitle(url)

    selection = inquirer.select(
        message="Select a subtitle language:",
        default=subtitles[0][0],
        choices=[lang for lang, _ in subtitles],
        pointer='=>',
        instruction='Use arrow keys to navigate and Enter to select.',
    ).execute()

    click.secho(f"You selected: {selection}", fg="green")

if __name__ == '__main__':
    cli()
