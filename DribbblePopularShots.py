import download
import json

# Get shot list
def downloadShotList_week(pageRange):
    shotList=[]
    output = open('PopularShotsWeek.csv', 'w')
    output.write('term,fre\n')
    Url = 'https://api.dribbble.com/v1/shots?page={}&timeframe=week&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'

    for pageNum in range(1,pageRange+1):
        Html = download.download(Url.format(pageNum))
        if Html != None:
            json_data = json.loads(Html)
            if json_data != []:
                for i in json_data:
                    print i['id']
                    shotList.append(i['id'])
                    output.write(str(i['id'])+'\n')

    return shotList

downloadShotList_week(50)