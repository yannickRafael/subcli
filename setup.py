from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(
    name="subcli",
    version="0.1.4",
    packages=find_packages(),
    install_requires=["click", "requests", "beautifulsoup4", "InquirerPy"],
    entry_points={
        "console_scripts": [
            "subcli=subcli.subcli:subcli",
        ],
    },
    author="yannickRafael",
    description="A CLI tool to download subtitles",
    long_description_content_type='text/markdown',
    long_description=description,
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.6",
)
