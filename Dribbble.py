import download
import csv
import time
def downloadArtist(username):
    artistUrl='https://dribbble.com/{}'

    artistHtml = download.download(artistUrl.format(username))
    if artistHtml != None:
        with open(username + '.html', 'w') as outfile:
            outfile.write(artistHtml)


readfile ='Dribbbles1000Users.csv'
with open(readfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        username=line['username']
        time.sleep(3)
        downloadArtist(username)