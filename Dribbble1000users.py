import download
import json
import time
name=[]
output=open('Dribbbles1000Users.csv', 'w')
output.write("username\n")
def downloadArtist(page):
    artistUrl='https://api.dribbble.com/v1/users/creativemints/followers?' \
              'page={}&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    artistHtml = download.download(artistUrl.format(page))
    if artistHtml != None:
        artistData = json.loads(artistHtml)
    if artistHtml ==None:
        artistData = "No user"
    return artistData


for page in range(502, 902):

    Data=downloadArtist(page)
    for record in Data:
        artistName = record["follower"]['username']
        name.append(artistName)
    time.sleep(1)
for i in set(name):
    output.write(str(i) + '\n')


