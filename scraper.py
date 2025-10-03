from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("https://www.mobileshop.eu/oppo/mobile-phones/find-n5-5g-dual-sim-512gb-16gb-ram/")
html = page.read().decode("utf-8")
print(html)
soup = BeautifulSoup(html, "html.parser")
