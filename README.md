# SubCLI – Subtitle Downloader from SubtitleCat

**SubCLI** é uma ferramenta de linha de comando (CLI) em Python que permite pesquisar e baixar legendas de filmes a partir do site [subtitlecat.com](https://subtitlecat.com), diretamente pelo terminal.

---

## Features

- Pesquisa de legendas por nome do filme  
- Escolha entre opções de idioma disponíveis  
- Download da legenda selecionada como arquivo `.zip`  
- Interface CLI interativa com navegação por setas  
- Baseado nas bibliotecas [Click](https://palletsprojects.com/p/click/) e [InquirerPy](https://github.com/kazhala/InquirerPy)

---

## Installation

> Requer **Python 3.6+**

### Opção 1 – Instalação via PyPI (recomendado)

```bash
pip install subcli
````

### Opção 2 – Instalação via Código-fonte

1. Clone o projeto:

```bash
git clone https://github.com/yourusername/subcli.git
cd subcli
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows use `.venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Instale o CLI localmente:

```bash
pip install .
```

---

## Usage

Depois da instalação, você pode rodar:

```bash
subcli "John Wick 4"
```

### O que acontece:

1. O programa busca resultados no SubtitleCat
2. Exibe uma lista de versões de legendas
3. Permite selecionar o idioma desejado
4. Faz o download da legenda `.zip` no diretório atual

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
│   ├── cli.py               # Ponto de entrada da CLI
│   └── get_subtitle.py      # Lógica de scraping e download
├── setup.py
├── README.md
└── requirements.txt
```

---

## Disclaimer

Este projeto realiza scraping de conteúdo do site [subtitlecat.com](https://subtitlecat.com). Use-o de forma responsável e respeite as licenças associadas às legendas.

---

## Author

Desenvolvido por yannickRafael – contribuições e forks são bem-vindos.

---

## License

MIT License

```