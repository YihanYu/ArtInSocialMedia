import download
import json
import time
name=[]
output=open('ArtStation1000Users.csv', 'w')
def downloadArtist(page):
    artistUrl='https://www.artstation.com/projects.json?page={}&sorting=latest'
    artistHtml = download.download(artistUrl.format(page))
    if artistHtml != None:
        artistData = json.loads(artistHtml)
    if artistHtml ==None:
        artistData = "No user"
    return artistData


for page in range(0, 20):

    Data=downloadArtist(page)
    for record in Data['data']:
        artistName = record['user']['username']
        name.append(artistName)
        print artistName

for i in set(name):
    output.write(i + '\n')