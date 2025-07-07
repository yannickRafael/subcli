import click
from get_subtitle import search_subtitle_options, get_subtitle, download_subtitle
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
    languages = get_subtitle(url)
    choices = list(languages.keys())

    selection = inquirer.select(
        message="Select a subtitle language:",
        default=choices[0],
        choices=choices,
        pointer='=>',
        instruction='Use arrow keys to navigate and Enter to select.',
    ).execute()

    click.secho(f"You selected: {selection}", fg="green")

    link = languages[selection]
    file = download_subtitle(link)
    click.secho(f"File downloaded as: {file}", fg="blue")

if __name__ == '__main__':
    cli()
