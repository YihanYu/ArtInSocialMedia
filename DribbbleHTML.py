from bs4 import BeautifulSoup
import os
output=open('walkDribbble.csv', 'w')
output.write('username,behance,artstation,facebook,google_plus,instagram,linkedin,pinterest,sketchfab,steam,tumblr,twitter,vimeo,youtube,deviantart\n')
#output=open('Dribbble-behance.csv', 'w')
#output.write("username\n")

for file in os.listdir('/Users/YihanYu/Desktop/NetworkAnalysis/RandomWalk/AllWalk/Dribbble'):
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
    UserSocial['deviantart'] = 0
    filename = os.path.basename(file)
    fileHandle = "/Users/YihanYu/Desktop/NetworkAnalysis/RandomWalk/AllWalk/Dribbble" + "//" + filename
    soup = BeautifulSoup(open(fileHandle), "lxml")
    website = soup.findAll("a", {"class": "elsewhere-website"})
    if website!=[]:
        link=website[0]['data-url']
    else:
        link=''
    username=filename.replace(".html","")
    if 'behance' in link:
        UserSocial['behance'] = 1
#        output.write(username+"\n")
    if soup.findAll("a", {"class": "elsewhere-behance"})!=[]:
        UserSocial['behance'] = 1
 #       output.write(username + "\n")
    if 'artstation' in link:
        UserSocial['artstation'] = 1
    if 'facebook' in link:
        UserSocial['facebook'] = 1
    if soup.findAll("a", {"class": "elsewhere-facebook"})!=[]:
        UserSocial['facebook'] = 1
    if 'plus.google' in link:
        UserSocial['google_plus'] = 1
    if 'linkedin' in link:
        UserSocial['linkedin'] = 1
    if soup.findAll("a", {"class": "elsewhere-linkedin"})!=[]:
        UserSocial['linkedin'] = 1
    if 'pinterest' in link:
        UserSocial['pinterest'] = 1
    if 'sketchfab_url' in link:
        UserSocial['sketchfab'] = 1
    if 'steamcommunity' in link:
        UserSocial['steam'] = 1
    if 'tumblr' in link:
        UserSocial['tumblr'] = 1
    if 'twitter' in link:
        UserSocial['twitter'] = 1
    if soup.findAll("a", {"class": "elsewhere-twitter"})!=[]:
        UserSocial['twitter'] = 1
    if 'vimeo' in link:
        UserSocial['vimeo'] = 1
    if soup.findAll("a", {"class": "elsewhere-vimeo"})!=[]:
        UserSocial['vimeo'] = 1
    if 'youtube' in link:
        UserSocial['youtube'] = 1
    if 'instagram' in link:
        UserSocial['instagram'] = 1
    if soup.findAll("a", {"class": "elsewhere-instagram"})!=[]:
        UserSocial['instagram'] = 1
    if 'deviantart' in link:
        UserSocial['deviantart'] = 1
    print UserSocial
    output.write(username+','+str(UserSocial['behance'])+","+str(UserSocial['artstation'])+","+str(UserSocial['facebook'])+","+str(UserSocial['google_plus'])+","+str(UserSocial['instagram'])+","+str(UserSocial['linkedin'])
                 + ","+str(UserSocial['pinterest'])+","+str(UserSocial['sketchfab'])+","+str(UserSocial['steam'])+","+str(UserSocial['tumblr'])+","+str(UserSocial['twitter'])+","+str(UserSocial['vimeo'])+","+str(UserSocial['youtube'])+","+str(UserSocial['deviantart'])+'\n')
