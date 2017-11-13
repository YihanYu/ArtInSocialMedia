import json
import csv
import download
import time

def downloadArtist(userID):
    artistUrl='https://www.deviantart.com/api/v1/oauth2/user/profile/{}?access_token=d7a0c12071e1d37768cda054ed2da52dd4c75ee68419722d8f'
    artistHtml = download.download(artistUrl.format(userID))
    if artistHtml!=None:
        artistData = json.loads(artistHtml)
        with open(str(userID)+'.json', 'w') as outfile:
            json.dump(artistData, outfile)

def getName(username):
    fileHandle = "/Users/YihanYu/Desktop/NetworkAnalysis/1000Users/ArtStation1000User" + "//" + username + ".json"
    json_data = open(fileHandle).read()
    data = json.loads(json_data)
    Link = data['deviantart_url']
    Name=Link.replace("https://", "").replace(".deviantart.com", "").replace("https//", "").replace("http://", "").replace("/", "")
    return Name



readfile="/Users/YihanYu/Desktop/NetworkAnalysis/RandomWalk/ArtStation-DeviantArt.csv"
with open(readfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        username=line['username']
        userID=getName(username)
        print userID
        time.sleep(5)
        downloadArtist(userID)