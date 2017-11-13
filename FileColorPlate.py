import download
from bs4 import BeautifulSoup

artistUrl = 'https://dribbble.com/shots/{}'

artistHtml = download.download(artistUrl.format('3452236-Player'))
soup = BeautifulSoup(artistHtml, "lxml")
user = soup.findAll("span", {"class": "shot-byline-user"})
for k in user:
    username=k.findAll("a")[0]["href"]
    website = soup.findAll("li", {"class": "color"})
    color = ''
    for i in website:
        for j in i.findAll("a"):
            colorUnit = str(j["title"])
            color = color + colorUnit + "|"
    print line['id']
    print username[1:]
    print line['created_at']
    print color[:-1]