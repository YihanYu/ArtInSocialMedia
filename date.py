import json
import os
import download
from datetime import datetime
import time

for file in os.listdir('/home/yyu41/Dribbble/FileLikes'):
    time.sleep(1)
    fileID=os.path.basename(file)[:7]
    outputfile=fileID+'.csv'
    output=open(outputfile, 'w')
    output.write('like_id,created_at,diff\n')
    print fileID
    Url = 'https://api.dribbble.com/v1/shots/{}?access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    Html = download.download(Url.format(fileID))
    if Html != None:
        pageData=json.loads(Html)
        shotTime=datetime.strptime(pageData['created_at'],'%Y-%m-%dT%H:%M:%SZ')
        file='/home/yyu41/Dribbble/FileLikes/'+file
        json_data= open(file).read()
        data = json.loads(json_data)
        for i in data:
            created_time=datetime.strptime(i['created_at'],'%Y-%m-%dT%H:%M:%SZ')
            diff=(created_time - shotTime).total_seconds()
            output.write(str(i['id'])+","+str(i['created_at'])+','+str(diff)+'\n')