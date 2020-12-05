import typing
from urllib.request import urlopen, Request
from urllib.parse import urljoin

from bs4 import BeautifulSoup

UA = 'Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'

def available(url: str) -> bool:
    req = Request(url, data=None, headers={'User-Agent': UA})
    with urlopen(req) as request:
        soup = BeautifulSoup(request.read(), features="html.parser")

    availability = soup.find('div', {'id': 'ProductBuy'})
    return not ("Sold Out" in availability.text)
