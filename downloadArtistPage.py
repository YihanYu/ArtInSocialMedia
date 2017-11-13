import download
import json

def downloadArtist(username):
    artistUrl='https://www.artstation.com/users/{}/projects.json?page={}'

    null=[]
    page=1

    while page!=0:

        artistHtml = download.download(artistUrl.format(username, page))
        artistData = json.loads(artistHtml)

        if artistData['data']!=null:
            print artistData['data']
            print type(artistData['data'])
            for record in artistData['data']:
                artworkID=record['id']
                artworkTitle=record['title']
                artworkDescription=record['description']
                artworkCreatedTime=record['created_at']
                hashID=record['hash_id']
            page+=1

        else:
            page=0


downloadArtist('kveldulv')