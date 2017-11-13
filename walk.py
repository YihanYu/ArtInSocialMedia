import csv
import download
import time
import json

def downloadArtist(userID):
    artistUrl='https://dribbble.com/{}'
    artistHtml = download.download(artistUrl.format(userID))
    if artistHtml != None:
        with open(username + '.html', 'w') as outfile:
            outfile.write(artistHtml)

def getName(username):
    fileHandle = "/Users/YihanYu/Desktop/NetworkAnalysis/1000Users/Behance1000Users" + "//" + username + ".json"
    json_data = open(fileHandle).read()
    data = json.loads(json_data)
    for i in data['user']['social_links']:
        if i['service_name']=="Dribbble":
            dribbblelink=i["url"]
            print dribbblelink
            behanceName = dribbblelink.replace("http://dribbble.com/", "")
            print behanceName
    return behanceName



readfile="/Users/YihanYu/PycharmProjects/ArtStation/Behance-Dribbble.csv"
with open(readfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        username=line['username']
        userID=getName(username)
        print userID
        downloadArtist(userID)
        time.sleep(3)