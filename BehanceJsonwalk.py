import json
import os
#output=open('Behance-Dribbble.csv',"w")
#output.write("username\n")
output=open('walkBehance_result.csv', 'w')
output.write('UserID,Google+,Instagram,Pinterest,Vimeo,Twitter,YouTube,LinkedIn,Tumblr,Facebook,Dribbble,Flickr,Etsy\n')

for file in os.listdir('/Users/YihanYu/Desktop/NetworkAnalysis/RandomWalk/AllWalk/Behance'):
    print file
    socialLink=[]
    UserSocial={}
    UserSocial['Google+']=0
    UserSocial['Instagram']=0
    UserSocial['Pinterest'] =0
    UserSocial['Vimeo'] = 0
    UserSocial['Twitter'] = 0
    UserSocial['YouTube'] = 0
    UserSocial['LinkedIn'] = 0
    UserSocial['Tumblr'] = 0
    UserSocial['Facebook'] = 0
    UserSocial['Dribbble'] = 0
    UserSocial['Flickr'] = 0
    UserSocial['Etsy'] = 0

    filename = os.path.basename(file)
    fileHandle = "/Users/YihanYu/Desktop/NetworkAnalysis/RandomWalk/AllWalk/Behance" + "//" + filename
    json_data= open(fileHandle).read()
    data = json.loads(json_data)
    UserSocial['UserID'] = data['user']['username']
    for i in data['user']['social_links']:
        socialLink.append(i['service_name'])
    if 'Google+' in socialLink:
        UserSocial['Google+'] = 1
    if 'Instagram' in socialLink:
        UserSocial['Instagram'] = 1
    if 'Pinterest' in socialLink:
        UserSocial['Pinterest'] = 1
    if 'Vimeo' in socialLink:
        UserSocial['Vimeo'] = 1
    if 'Twitter' in socialLink:
        UserSocial['Twitter'] = 1
    if 'YouTube' in socialLink:
        UserSocial['YouTube'] = 1
    if 'LinkedIn' in socialLink:
        UserSocial['LinkedIn'] = 1
    if 'Tumblr' in socialLink:
        UserSocial['Tumblr'] = 1
    if 'Facebook' in socialLink:
        UserSocial['Facebook'] = 1
    if 'Dribbble' in socialLink:
        UserSocial['Dribbble'] = 1
 #       output.write(UserSocial['UserID']+"\n")
    if 'Flickr' in socialLink:
        UserSocial['Flickr'] = 1
    if 'Etsy' in socialLink:
        UserSocial['Etsy'] = 1
    print UserSocial
    output.write(str(UserSocial['UserID'])+","+str(UserSocial['Google+'])+","+str(UserSocial['Instagram'])+","+str(UserSocial['Pinterest'])+","+str(UserSocial['Vimeo'])+","+str(UserSocial['Twitter'])
                 + ","+str(UserSocial['YouTube'])+","+str(UserSocial['LinkedIn'])+","+str(UserSocial['Tumblr'])+","+str(UserSocial['Facebook'])+","+str(UserSocial['Dribbble'])+","+str(UserSocial['Flickr'])+","+str(UserSocial['Etsy'])+'\n')