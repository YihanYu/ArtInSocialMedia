import json
import os
import download
from datetime import datetime
import time

outputfile='shotCreatedTime.csv'
output=open(outputfile, 'w')
output.write('shotID,createdTime\n')

for file in os.listdir('/home/yyu41/Dribbble/FileLikes_csv'):
    time.sleep(1)
    fileID=os.path.basename(file)[:7]
    print fileID
    Url = 'https://api.dribbble.com/v1/shots/{}?access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    Html = download.download(Url.format(fileID))
    if Html != None:
        pageData=json.loads(Html)
        shotTime=pageData['created_at']
        output.write(fileID+','+shotTime+'\n')