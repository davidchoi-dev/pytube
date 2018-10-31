import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class Video:
    def __init__(self, title, url):
          self.title = title
          self.url = url

videos = []
my_url = 'http://www.youtube.com/results?search_query=iu'

# opening up connection, grabbing the content
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("a", {"class": "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})

for i, container in enumerate(containers):
    videos.append(Video(container["title"], container["href"]))

input = input()
print(videos[int(input)].url)
