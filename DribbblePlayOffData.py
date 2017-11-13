import download
import json

# Get playoffs list
def downloadPlayoffList(pageRange):
    playoffList=[]
    Url = 'https://api.dribbble.com/v1/shots?list=playoffs&page={}&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'

    for pageNum in range(1,pageRange+1):
        Html = download.download(Url.format(pageNum))
        if Html != None:
            json_data = json.loads(Html)
            if json_data != []:
                for i in json_data:
                    playoffList.append(i['id'])
    return playoffList

# List rebounds for a shot
def downloadReboundList(playoffID):
    reboundsList=[]
    Url = 'https://api.dribbble.com/v1/shots/{}/rebounds?page={}&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    page=1
    while True:
        Html = download.download(Url.format(playoffID, page))
        if Html != None:
            json_data = json.loads(Html)
            if json_data != []:
                for i in json_data:
                    reboundsList.append(i['id'])
            page=page+1
        if json_data==[]:
            break
    return reboundsList

# Download shot info
def downloadInfo(id):
    outfile = open(str(id) + '_Info' + '.json', 'w')
    shotUrl = 'https://api.dribbble.com/v1/shots/{}?access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    shotHtml = download.download(shotUrl.format(id))
    json_data = json.loads(shotHtml)
    json.dump(json_data, outfile)

# Download shot comments
def downloadComments(id):
    outfile = open(str(id)+'_Comments' + '.json', 'w')
    shotUrl = 'https://api.dribbble.com/v1/shots/{}/comments?page={}&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    page=1
    Data=[]
    while True:
        shotHtml = download.download(shotUrl.format(id,page))
        if shotHtml != None:
            json_data = json.loads(shotHtml)
            if json_data != []:
                Data=Data+json_data
                print page
                page = page + 1
            if json_data == []:
                break
    json.dump(Data, outfile)