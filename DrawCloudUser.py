import download
import json
import time
name=[]
output=open('DrawCloud1000Users.csv', 'w')
def downloadArtist(page):
    artistUrl='https://drawcrowd.com/rankings.json?limit=200&type=daily&date=2016-10-0{}'
    artistHtml = download.download(artistUrl.format(page))
    if artistHtml != None:
        artistData = json.loads(artistHtml)
    if artistHtml ==None:
        artistData = "No user"
    return artistData


for page in range(1, 10):

    Data=downloadArtist(page)
    for record in Data['project_rankings']:
        artistName = record['user_id']
        name.append(artistName)

for i in set(name):
    output.write(str(i) + '\n')