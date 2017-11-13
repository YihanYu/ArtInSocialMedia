import download
import json
import time
offset=0

output=open('DeviantArt1000Users3.csv', 'w')
output.write('username\n')
def downloadArtist(username, offSet):
    artistUrl='https://www.deviantart.com/api/v1/oauth2/user/friends/{}?offset={}&access_token=2d5a765dbc1b29c015008880a7cd3652e4dcad99458488a06f'
    artistHtml = download.download(artistUrl.format(username, offSet))
    if artistHtml != None:
        artistData = json.loads(artistHtml)
    if artistHtml ==None:
        artistData = "No user"
    return artistData


for offset in range(0, 5000, 10):

    Zarla=downloadArtist('cryptid-creations', offset)
    time.sleep(5)
    for record in Zarla['results']:
        user=record['user']
        artistName = user['username']
        output.write(artistName + '\n')
    if Zarla['has_more']== True:
        print "yes"
        print offset
    else:
        break

