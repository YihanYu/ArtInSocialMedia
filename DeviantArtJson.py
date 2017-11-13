import json
import os
output=open('walkDeviantArt.csv', 'w')
output.write('username,behance,artstation,facebook,google_plus,instagram,linkedin,pinterest,sketchfab,steam,tumblr,twitter,vimeo,youtube,dribbble\n')

for file in os.listdir('/Users/YihanYu/Desktop/NetworkAnalysis/RandomWalk/AllWalk/DeviantArt'):
    print file
    UserSocial = {}
    UserSocial['behance'] = 0
    UserSocial['artstation'] = 0
    UserSocial['facebook'] = 0
    UserSocial['google_plus'] = 0
    UserSocial['linkedin'] = 0
    UserSocial['pinterest'] = 0
    UserSocial['sketchfab'] = 0
    UserSocial['steam'] = 0
    UserSocial['tumblr'] = 0
    UserSocial['twitter'] = 0
    UserSocial['vimeo'] = 0
    UserSocial['youtube'] = 0
    UserSocial['instagram'] = 0
    UserSocial['dribbble'] = 0
    filename = os.path.basename(file)
    fileHandle = "/Users/YihanYu/Desktop/NetworkAnalysis/RandomWalk/AllWalk/DeviantArt" + "//" + filename
    json_data= open(fileHandle).read()
    data = json.loads(json_data)
    username = data['user']['username']

    bio=data['bio']
    if 'behance' in bio:
        UserSocial['behance'] = 1
    if 'artstation' in bio:
        UserSocial['artstation'] = 1
    if 'facebook' in bio:
        UserSocial['facebook'] = 1
    if 'plus.google' in bio:
        UserSocial['google_plus'] = 1
    if 'linkedin' in bio:
        UserSocial['linkedin'] = 1
    if 'pinterest' in bio:
        UserSocial['pinterest'] = 1
    if 'sketchfab_url' in bio:
        UserSocial['sketchfab'] = 1
    if 'steamcommunity' in bio:
        UserSocial['steam'] = 1
    if 'tumblr' in bio:
        UserSocial['tumblr'] = 1
    if 'twitter' in bio:
        UserSocial['twitter'] = 1
    if 'vimeo' in bio:
        UserSocial['vimeo'] = 1
    if 'youtube' in bio:
        UserSocial['youtube'] = 1
    if 'instagram' in bio:
        UserSocial['instagram'] = 1
    if 'dribbble' in bio:
        UserSocial['dribbble'] = 1
    print UserSocial
    output.write(username+','+str(UserSocial['behance'])+","+str(UserSocial['artstation'])+","+str(UserSocial['facebook'])+","+str(UserSocial['google_plus'])+","+str(UserSocial['instagram'])+","+str(UserSocial['linkedin'])
                 + ","+str(UserSocial['pinterest'])+","+str(UserSocial['sketchfab'])+","+str(UserSocial['steam'])+","+str(UserSocial['tumblr'])+","+str(UserSocial['twitter'])+","+str(UserSocial['vimeo'])+","+str(UserSocial['youtube'])+","+str(UserSocial['dribbble'])+'\n')
