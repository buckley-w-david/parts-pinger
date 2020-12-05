import typing
from urllib.request import urlopen, Request
from urllib.parse import urljoin

from bs4 import BeautifulSoup

UA = 'Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'

def available(url: str) -> bool:
    req = Request(url, data=None, headers={'User-Agent': UA})
    with urlopen(req) as request:
        soup = BeautifulSoup(request.read(), features="html.parser")

    online = 'Out of Stock' not in soup.find(class_='c-capr-inventory-selector__details-online').text
    online = online and 'Backorder' not in soup.find(class_='c-capr-inventory-selector__details-online').text
    london = 'Out of Stock' not in soup.find('li', {"data-region-name": 'Ontario'}).select(".c-capr-inventory-region li:nth-child(2) span:nth-child(2)")[0].text
    london = london and 'Backorder' not in soup.find('li', {"data-region-name": 'Ontario'}).select(".c-capr-inventory-region li:nth-child(2) span:nth-child(2)")[0].text

    return online or london
