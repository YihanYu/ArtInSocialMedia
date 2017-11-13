import json
import csv
import download

def downloadArtist(userID):
    artistUrl='https://api.behance.net/v2/users/{}?client_id=BnTmyF57LQE5u9usKCwsT6ikawzRWIYD'
    artistHtml = download.download(artistUrl.format(userID))
    if artistHtml != None:
        artistData = json.loads(artistHtml)
        with open(str(userID)+'.json', 'w') as outfile:
            json.dump(artistData, outfile)

def getName(username):
    fileHandle = "/Users/YihanYu/Desktop/NetworkAnalysis/1000Users/ArtStation1000User" + "//" + username + ".json"
    json_data = open(fileHandle).read()
    data = json.loads(json_data)
    behanceLink = data['behance_url']
    behanceName=behanceLink.replace("https://www.behance.net/", "").replace("https://behance.net/", "")
    return behanceName




readfile="/Users/YihanYu/Desktop/NetworkAnalysis/RandomWalk/ArtStation-Behance.csv"
with open(readfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        username=line['username']
        print username
        userID=getName(username)
        downloadArtist(userID)



