from pathlib import Path
import typer
import toml

from parts_pinger import scrapers

from dataclasses import dataclass

@dataclass
class PartConfig:
    url: str
    scraper: str
    name: str = 'n/a'

app = typer.Typer()
@app.command()
def scrape(config_file: Path = Path('config.toml')):
    config = toml.load(config_file)
    for part in (PartConfig(**part) for part in config['Parts']):
        scraper = getattr(scrapers, part.scraper)
        try:
            if scraper.available(part.url):
                print(part.name, "is available!")
            else:
                print(part.name, "is not available :(")
        except:
            print(part.name, "is not available :(")

if __name__ == '__main__':
    app()
