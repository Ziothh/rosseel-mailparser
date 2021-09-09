from setuptools import setup, find_packages

setup(
    name="rosseel-mailparser",
    version="1.2.5",
    description="This package is used in Agence Rosseel to parse mail content(leads, excel, ...) and send it to their webhook",
    author="Louis Giët",
    author_email="louisgiet.w@gmail.com",
    url="githubrepourl",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "parser-run = mailparser_app:main"
        ]
    },
    install_requires=[
        "beautifulsoup4",
        "lxml",
        "requests", 
        "pandas", 
        "regex",
    ]
)