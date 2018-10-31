import webbrowser as wb
from colorama import init, Fore, Back, Style
from termcolor import colored
import bs4
import os
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
init(autoreset=True)

class Video:
    def __init__(self, title, url):
          self.title = title
          self.url = url

videos = []

# make a query
url = 'http://www.youtube.com/results?search_query='
print(Fore.GREEN + 'pyTube> ', end='')
q = input()
url += q
os.system( 'cls' )
print('Browsing ...')
# item limitation to fetch
limit = 5

# opening up connection, grabbing the content
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("a", {"class": "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})[:limit]
os.system( 'cls' )

for i, container in enumerate(containers):
    videos.append(Video(container["title"], container["href"]))
    print(Fore.GREEN + str(i) + '.', container["title"])

print(Fore.GREEN + 'pyTube?> ', end='')
input = input()
wb.open_new('http://www.youtube.com' + videos[int(input)].url)