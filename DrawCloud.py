import download
import json
import csv
import time

def downloadArtist(userID):
    artistUrl='https://drawcrowd.com/users/{}.json'
    artistHtml = download.download(artistUrl.format(userID))
    if artistHtml!=None:
        artistData = json.loads(artistHtml)
        with open(str(userID)+'.json', 'w') as outfile:
            json.dump(artistData, outfile)

readfile ='DrawCloud1000Users.csv'
with open(readfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        userid=line['id']
        time.sleep(2)
        downloadArtist(userid)