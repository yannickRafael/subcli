from setuptools import setup, find_packages

setup(
    name="subcli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click", "requests", "beautifulsoup4", "InquirerPy"],
    entry_points={
        "console_scripts": [
            "subcli=subtitle_downloader.cli:download",
        ],
    },
    author="yannickRafael",
    description="A CLI tool to download subtitles",
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.6",
)
