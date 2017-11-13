import download
import json


maxmumPages=10
sortingMethod='trending'
#sortingMethod='community'
#sortingMethod='latest'
#sortingMethod='picks'
#sortingMethod='streams'

url='https://www.artstation.com/projects.json?page={}&sorting={}'

for page in range(1, maxmumPages):

    html=download.download(url.format(page,sortingMethod))
    data=json.loads(html)
    for record in data['data']:
        user= record['user']
        username=user['username']
        userID=record['user_id']
        description=record['description']
        title=record['title']
        createdTime=record['created_at']
        hashID=record['hash_id']
        likesCount=record['likes_count']
        viewsCount=record['views_count']



