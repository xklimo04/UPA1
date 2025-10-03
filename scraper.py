import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

for line in sys.stdin:
    line = line.strip()
    page = urlopen(line)
    html = page.read().decode("utf-8")
    soup =  BeautifulSoup(html, "html.parser")
    
    # Print URL
    print(line, "\t", end="")
    
    # Print product name
    try:
        name = soup.find("h1", class_="product-name").text.strip()
    except Exception:
        name = ""
    print(name, "\t", end="")
    
    # Print price
    try:
        price = soup.find("div", class_="price").text.strip()
    except Exception:
        price = ""
    print(price, "\t", end="")
    
    # Print memory
    try:
        memory = soup.find("dt", string="vnitřní:").find_next_sibling("dd").text.strip()
    except Exception:
        memory = ""
    print(memory, "\t", end="")
    
    # Print battery
    try:
        battery = soup.find("dt", string="Nabíjení:").find_next_sibling("dt").find_next_sibling("dd").text.strip()
    except Exception:
        battery = ""
    print(battery, "\t", end="")
    
    # Print weight
    try:
        weight = soup.find("dt", string="Hmotnost:").find_next_sibling("dd").text.strip()
    except Exception:
        weight = ""
    print(weight, "\t", end="")
    
    # Print SD
    try:
        sd = soup.find("dt", string="Slot pro karty:").find_next_sibling("dd").text.strip()
    except Exception:
        sd = ""
    print(sd, "\t", end="")
    
    # Print CPU
    try:
        cpu = soup.find("dt", string="CPU:").find_next_sibling("dd").text.strip()
    except Exception:
        cpu = ""
    print(cpu)

