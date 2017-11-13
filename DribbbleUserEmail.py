import json
import download
import re
import time

regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                    "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                    "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

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
    name=[]
    while True:
        shotHtml = download.download(shotUrl.format(id,page))
        if shotHtml != None:
            comData = json.loads(shotHtml)
            if comData!= []:
                for comment in comData:
                    name.append(comment['user']['username'])
                page = page + 1
            if comData == []:
                break
    return set(name)

def downloadUserInfo(username):
    userUrl = 'https://api.dribbble.com/v1/users/{}?access_token=9a7123861f629b903d04c7fdd6d6ed00c124c6d44af05b7c8e9ae9f079064d95'
    userHtml = download.download(userUrl.format(username))
    userData = json.loads(userHtml)
    name=userData['username'].encode('ascii', 'ignore')
    location=userData['location']
    if location!=None:
        location=location.encode('ascii', 'ignore').replace(",", ".")

    bio=userData['bio']
    print bio
    email = re.findall(regex,bio)
    print email
    if email!=[]:
        for i in email:
            emailAdress= i[0]
    else:
        emailAdress='NA'
    buckets_count=userData['buckets_count']
    comments_received_count=userData['comments_received_count']
    followers_count=userData['followers_count']
    followings_count=userData['followings_count']
    likes_count=userData['likes_count']
    likes_received_count=userData['likes_received_count']
    projects_count=userData['projects_count']
    rebounds_received_count=userData['rebounds_received_count']
    shots_count=userData['shots_count']
    teams_count=userData['teams_count']
    output.write(name + ','+str(location)+',')
    output.write(str(buckets_count)+',')
    output.write(str(comments_received_count) + ',')
    output.write(str(followers_count) + ',')
    output.write(str(followings_count) + ',')
    output.write(str(likes_count) + ',')
    output.write(str(likes_received_count) + ',')
    output.write(str(projects_count) + ',')
    output.write(str(rebounds_received_count) + ',')
    output.write(str(shots_count) + ',')
    output.write(str(teams_count) + ',')
    output.write(emailAdress+'\n')

output=open('Dribbbles1000Users.csv', 'w')
output.write('name,location,buckets,comments_received,followers,followings,likes,likes_received,projects,rebounds_received,shots,teams,email\n')
playoffID=2315215
userList=downloadComments(playoffID)
for user in userList:
    print downloadUserInfo(user)
    time.sleep(1)
