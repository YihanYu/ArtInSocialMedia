import download
import json


def downloadUserShots(user_id):
    userUrl = 'https://api.dribbble.com/v1/users/{}/shots?page={}&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    page=1
    while True:
        userHtml = download.download(userUrl.format(user_id,page))
        if userHtml != None:
            userData = json.loads(userHtml)
            if userData!= []:
                for shot in userData:
                    print shot['images']['hidpi']
                page = page + 1
            if userData == []:
                break

downloadUserShots(283823)
