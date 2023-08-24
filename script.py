import requests
import re
from bs4 import BeautifulSoup

twoDShapes = []

url = 'https://en.wikipedia.org/wiki/List_of_two-dimensional_geometric_shapes'
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
locator = 'div#mw-content-text > div.mw-parser-output ul li a'

extractedSoup = soup.css.select(locator)

for tag in extractedSoup[:-3]:  # last 3 elements are: 'List of triangle topics', 'List of circle topics', 'Glossary of shapes with metaphorical names'
    twoDShapes.append(tag.text)

for i in range(0, 2255):
    with open(f"C:\\users\\scrab\\Downloads\\Logs\\Logs\\log_{i}.xml", encoding="UTF-8") as file:
        lines = file.read()
        for shape in twoDShapes:
            exp = f'\W{shape}\W'
            if re.search(exp, lines):
                print(f'Shape: {shape}, File: {i}')