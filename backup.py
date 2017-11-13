# Download shot comments
def downloadComments(id):
    outfile = open(str(id)+'_Comments' + '.json', 'w')
    shotUrl = 'https://api.dribbble.com/v1/shots/{}/comments?page={}&access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    page=1
    while True:
        shotHtml = download.download(shotUrl.format(id,page))
        if shotHtml != None:
            json_data = json.loads(shotHtml)
            if json_data != []:
                json.dump(json_data, outfile)
                print page
                page = page + 1
            if json_data == []:
                break