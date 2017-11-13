import download
import json
import time
import re
a=[]
output = open('DribbblePlayoff4.csv', 'w')
def downloadArtwork(id,page):
    artistUrl='https://api.dribbble.com/v1/shots/{}/comments?page={}&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    artistHtml = download.download(artistUrl.format(id,page))
    if artistHtml != None:
        json_data = json.loads(artistHtml)
        return json_data

for i in range(1,10):
    page=i
    data=downloadArtwork('2989710-Dribbble-Side-Panel', page)
    if data!=[]:
        for j in data:
            b=[]
            print type(j['user']['name'])
            print j['user']['name'].encode('ascii','replace')
            match=re.findall('@([A-Za-z0-9\s]+)', j['body'])
            print match
            if match==[]:
                b.append(j['user']['name'].encode('ascii','replace'))
                b.append('Dan Cederholm')
                a.append(b)
            else:
                for k in match:
                    b=[]
                    print type(k)
                    b.append(j['user']['name'].encode('ascii','replace'))
                    b.append(k.encode('ascii','replace'))
                    a.append(b)
    else:
        break
    time.sleep(3)
print a
for group in a:
    output.write(str(group)+"\n")