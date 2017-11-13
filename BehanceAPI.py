import download
import json
import csv


def downloadArtist(userID):
    artistUrl='https://api.behance.net/v2/users/{}?client_id=BnTmyF57LQE5u9usKCwsT6ikawzRWIYD'
    artistHtml = download.download(artistUrl.format(userID))
    if artistHtml != None:
        artistData = json.loads(artistHtml)
        with open(str(userID)+'.json', 'w') as outfile:
            json.dump(artistData, outfile)

readfile ='Behance1000Users.csv'
with open(readfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        userid=line['id']
        downloadArtist(userid)




