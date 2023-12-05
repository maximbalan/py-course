import requests
from icecream import ic
from bs4 import BeautifulSoup

url = "https://openai.com/blog"

r = requests.get(url)
c = r.content

soup = BeautifulSoup(c, "html.parser")
header_titles = soup.find_all(["h1","h2","h3","h4","h5","h6"])

for header in header_titles:
    ic(header.text.strip())