# SubCLI – Subtitle Downloader from SubtitleCat

**SubCLI** is a Python command-line interface (CLI) tool that allows you to search and download movie subtitles from [subtitlecat.com](https://subtitlecat.com), directly from your terminal.

---

## Features

- Search for subtitles by movie name  
- Choose from available language options  
- Download the selected subtitle as a `.zip` file  
- Interactive CLI interface with arrow key navigation  
- Built using [Click](https://palletsprojects.com/p/click/) and [InquirerPy](https://github.com/kazhala/InquirerPy)

---

## Installation

> Requires **Python 3.6+**

### Option 1 – Install from PyPI (recommended)

```bash
pip install subcli
````

### Option 2 – Install from source

1. Clone the repository:

```bash
git clone https://github.com/yourusername/subcli.git
cd subcli
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Install the CLI locally:

```bash
pip install .
```

---

## Usage

After installation, you can run:

```bash
subcli "John Wick 4"
```

### What happens:

1. The program searches for subtitle results on SubtitleCat
2. Displays a list of subtitle versions
3. Lets you select the desired language
4. Downloads the subtitle `.zip` into the current directory

---

## Example

```bash
$ subcli "The Matrix"

Found 12 subtitles for 'The Matrix':
? Select a subtitle result: (Use arrow keys)
=> The Matrix 1999 BluRay x264 YIFY
   The Matrix 1999 DVDRip
   The Matrix Reloaded 2003

? Select a subtitle language: (Use arrow keys)
=> English
   Portuguese
   Spanish

You selected: English
File downloaded as: The.Matrix.1999.YIFY.English.zip
```

---

## Project Structure

```
subcli/
├── subcli/
│   ├── __init__.py
│   ├── cli.py               # CLI entry point
│   └── get_subtitle.py      # Scraping and download logic
├── setup.py
├── README.md
└── requirements.txt
```

---

## Disclaimer

This project scrapes content from [subtitlecat.com](https://subtitlecat.com). Use it responsibly and respect the licensing terms associated with subtitle files.

---

## Author

Developed by yannickRafael – contributions and forks are welcome.

---

## License

MIT License

```