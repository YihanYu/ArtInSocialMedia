import download
import json

def downloadArtwork(hashId):
    artworkUrl='https://www.artstation.com/projects/{}/comments.json'

    artworkHtml = download.download(artworkUrl.format(hashId))
    artworkData = json.loads(artworkHtml)
    for record in artworkData['data']:
        username=record['user']['username']
        text=record['text']


downloadArtwork('3mOXE')