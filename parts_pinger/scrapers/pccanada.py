import typing
from urllib.request import urlopen, Request
from urllib.parse import urljoin

import re

from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': ' Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0' ,
    'Accept': ' text/html, */*; q=0.01' ,
    'Accept-Language': ' en-US,en;q=0.5' ,
    'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8' ,
    'X-Requested-With': ' XMLHttpRequest' ,
    'Origin': ' https://www.pc-canada.com' ,
    'DNT': ' 1' ,
    'Connection': ' keep-alive' ,
}

def available(url: str) -> bool:
    item_id = re.search(r"https://www\.pc-canada\.com/item/(.*)\.html", url).group(1)

    req = Request('https://www.pc-canada.com/p/item/rts/itemdiv.asp', data=bytes(f'item={item_id}', encoding='utf-8'), headers=HEADERS)
    with urlopen(req) as request:
        soup = BeautifulSoup(request.read(), features="lxml")

    return soup.find("span", {"id": "RTS_TotalStock"}).text != "0"
