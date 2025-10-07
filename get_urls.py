from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlsplit, urlunsplit, quote

url = "https://www.mobileshop.eu/cz/android-os/"

def encode_url(url: str) -> str:
    parts = urlsplit(url)
    path = quote(parts.path, safe="/%")
    query = quote(parts.query, safe="=&%")
    fragment = quote(parts.fragment, safe="")
    return urlunsplit((parts.scheme, parts.netloc, path, query, fragment))

i = 0
iterate = True

while(iterate):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.select("#mainContent")[0].find_all("h5")

    for row in rows:
        if 150 <= i:
            iterate = not iterate
            break
        href = row.find("a")['href']
        href = "https://www.mobileshop.eu" + href 
        print(encode_url(href))
        i = i + 1

    if iterate:
        try: 
            nextpage = soup.find("nav", class_ = "pager").find("a", string="DALŠÍ")['href']
            url = "https://www.mobileshop.eu" + nextpage
        except:
            iterate = not iterate