import download
import json
from bs4 import BeautifulSoup


artistUrl = 'https://dribbble.com/shots/{}'

# Get playoffs list
def downloadPlayoffList(pageRange):
    playoffList=[]
    Url = 'https://api.dribbble.com/v1/shots?list=playoffs&page={}' \
          '&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'

    for pageNum in range(1,pageRange+1):
        Html = download.download(Url.format(pageNum))
        if Html != None:
            json_data = json.loads(Html)
            if json_data != []:
                for i in json_data:
                    playoffList.append(i['id'])
                    playoffID= i['id']
                    userName= i['user']['name']
                    createdAt= i['created_at']
                    color= ''
                    artistHtml = download.download(artistUrl.format(i['id']))
                    soup = BeautifulSoup(artistHtml, "lxml")
                    website = soup.findAll("li", {"class": "color"})
#                    print website
                    for i in website:
                        for j in i.findAll("a"):
#                            print j['title']
                            colorUnit= str(j["title"])
                            color=color+colorUnit+"|"
                    print playoffID
                    print userName
                    print createdAt
                    print color

downloadPlayoffList(1)
