from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='parts_pinger',
    version='0.1.0',
    author='David Buckley',
    author_email='david@davidbuckley.ca',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'lxml',
        'toml',
        'typer',
    ],
    entry_points = {
        'console_scripts': [
            'parts-pinger=parts_pinger.cli:app'
        ]
    }
)
