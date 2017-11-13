import json
import os

#output=open('ArtStation.csv', 'w')
#output.write('username,behance,deviantart,facebook,google_plus,instagram,linkedin,pinterest,sketchfab,steam,tumblr,twitter,vimeo,youtube\n')

for file in os.listdir('/Users/YihanYu/Desktop/ArtStation1000User'):
    UserSocial={}
    UserSocial['behance']=0
    UserSocial['deviantart']=0
    UserSocial['facebook']=0
    UserSocial['google_plus']=0
    UserSocial['linkedin']=0
    UserSocial['pinterest']=0
    UserSocial['sketchfab']=0
    UserSocial['steam']=0
    UserSocial['tumblr']=0
    UserSocial['twitter']=0
    UserSocial['vimeo']=0
    UserSocial['youtube']=0
    UserSocial['instagram']=0
    filename = os.path.basename(file)
    fileHandle = "/Users/YihanYu/Desktop/ArtStation1000User" + "//" + filename
    json_data= open(fileHandle).read()
    data = json.loads(json_data)
    username=data['username']
    if data['behance_url']!=None:
        UserSocial['behance']=1
    if data['deviantart_url']!=None:
        UserSocial['deviantart']=1
    if data['facebook_url']!=None:
        UserSocial['facebook']=1
    if data['google_plus_url']!=None:
        UserSocial['google_plus']=1
    if data['linkedin_url']!=None:
        UserSocial['linkedin']=1
    if data['pinterest_url']!=None:
        UserSocial['pinterest']=1
    if data['sketchfab_url']!=None:
        UserSocial['sketchfab']=1
    if data['steam_url']!=None:
        UserSocial['steam']=1
    if data['tumblr_url']!=None:
        UserSocial['tumblr']=1
    if data['twitter_url']!=None:
        UserSocial['twitter']=1
    if data['vimeo_url']!=None:
        UserSocial['vimeo']=1
    if data['youtube_url']!=None:
        UserSocial['youtube']=1
    if data['instagram_url']!=None:
        UserSocial['instagram']=1
        print data['instagram_url']
#    output.write(username+','+str(UserSocial['behance'])+","+str(UserSocial['deviantart'])+","+str(UserSocial['facebook'])+","+str(UserSocial['google_plus'])+","+str(UserSocial['instagram'])+","+str(UserSocial['linkedin'])
#                 + ","+str(UserSocial['pinterest'])+","+str(UserSocial['sketchfab'])+","+str(UserSocial['steam'])+","+str(UserSocial['tumblr'])+","+str(UserSocial['twitter'])+","+str(UserSocial['vimeo'])+","+str(UserSocial['youtube'])+'\n')