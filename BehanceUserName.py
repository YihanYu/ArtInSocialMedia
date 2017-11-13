import download
import json
output=open('Behance1000Users.csv', 'w')
output.write('id\n')

def downloadArtist(page):
    artistUrl='https://api.behance.net/v2/users?page={}&client_id=BnTmyF57LQE5u9usKCwsT6ikawzRWIYD'
    artistHtml = download.download(artistUrl.format(page))
    if artistHtml != None:
        artistData = json.loads(artistHtml)
    if artistHtml ==None:
        artistData = "No user"
    return artistData


for page in range(0, 120):

    Data=downloadArtist(page)
    for record in Data['users']:
        artistName = record['id']
        output.write(str(artistName)+'\n')
        print artistName

