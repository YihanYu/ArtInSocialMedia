import download
import json
import csv
import time

def downloadArtist(userID):
    artistUrl='https://www.deviantart.com/api/v1/oauth2/user/profile/{}?access_token=d67750c46ae004e68cd6cea0716c5ec8c354908e929ff5f469'
    artistHtml = download.download(artistUrl.format(userID))
    if artistHtml!=None:
        artistData = json.loads(artistHtml)
        with open(str(userID)+'.json', 'w') as outfile:
            json.dump(artistData, outfile)

readfile ='DeviantArt1000Users.csv'
with open(readfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        userid=line['id']
#        time.sleep(5)
        downloadArtist(userid)