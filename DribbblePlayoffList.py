import download
import json
import time

Url = 'https://api.dribbble.com/v1/shots?list=playoffs&page={}&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
pageNum=1
while True:
    Html = download.download(Url.format(pageNum))
    if Html != None:
        json_data = json.loads(Html)
        if json_data != []:
            outfile = open('PlayOff'+'PageNum'+str(pageNum) + '.json', 'w')
            json.dump(json_data, outfile)
        pageNum = pageNum+ 1
        time.sleep(3)
    if Html == None:
            break


