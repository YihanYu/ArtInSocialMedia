import googleAPI
import colorsys
import matplotlib.colors as colors
import math

R=100.00
angle=30.00
h = R * math.cos(angle / 180 * math.pi)
r = R * math.sin(angle / 180 * math.pi)

# Data from userid 322178
l1='https://cdn.dribbble.com/users/322178/screenshots/3527817/petrichor-shot_1x.jpg'
l2='https://cdn.dribbble.com/users/322178/screenshots/3512286/fix.me_1x.jpg'
l3='https://cdn.dribbble.com/users/322178/screenshots/3512244/wilbur-go-dribbble_1x.jpg'
l4='https://cdn.dribbble.com/users/322178/screenshots/3422872/squid-ink_1x.jpg'
l5='https://cdn.dribbble.com/users/322178/screenshots/2376390/mortgage-cover_1x.jpg'
l6='https://cdn.dribbble.com/users/322178/screenshots/2372423/bru-1_1x.jpg'
l7='https://cdn.dribbble.com/users/322178/screenshots/1869240/michigan_1x.jpg'
l8='https://cdn.dribbble.com/users/322178/screenshots/1860477/liberty-me-1_1x.jpg'
l9='https://cdn.dribbble.com/users/322178/screenshots/1662927/credit-score-widget-v2_1x.jpg'
l10='https://cdn.dribbble.com/users/322178/screenshots/1330979/screen_shot_2013-12-01_at_11.52.18_pm.png'
l11='https://cdn.dribbble.com/users/322178/screenshots/1155467/monstercheck-app_1x.jpg'
l12='https://cdn.dribbble.com/users/322178/screenshots/1149439/its-time_1x.jpg'
l13='https://cdn.dribbble.com/users/322178/screenshots/1145307/my-credit-dashboard.jpg'
l14='https://cdn.dribbble.com/users/322178/screenshots/1145167/green-team-logo-400.jpg'
l15='https://cdn.dribbble.com/users/322178/screenshots/1143600/11_1x.jpg'

c1=googleAPI.googleAPI(l1)
c2=googleAPI.googleAPI(l2)
c3=googleAPI.googleAPI(l3)
c4=googleAPI.googleAPI(l4)
c5=googleAPI.googleAPI(l5)
c6=googleAPI.googleAPI(l6)
c7=googleAPI.googleAPI(l7)
c8=googleAPI.googleAPI(l8)
c9=googleAPI.googleAPI(l9)
c10=googleAPI.googleAPI(l10)
c11=googleAPI.googleAPI(l11)
c12=googleAPI.googleAPI(l12)
c13=googleAPI.googleAPI(l13)
c14=googleAPI.googleAPI(l14)
c15=googleAPI.googleAPI(l15)

def hex_to_hsv(hexString):
    RGBValue= colors.hex2color(hexString)
    return colorsys.rgb_to_hsv(RGBValue[0], RGBValue[1], RGBValue[2])

def rgb_to_hsv_palette(colorPalette):
    hsvPalette=[]
    for rgbw in colorPalette:
        hsv = colorsys.rgb_to_hsv(float(rgbw[0])/255, float(rgbw[1])/255, float(rgbw[2])/255)
        print hsv
        hsvColor=[]
        hsvColor.append(hsv)
        hsvColor.append(rgbw[3])
        hsvPalette.append(hsvColor)
    return hsvPalette

def color_distance(hsv1,hsv2):
    x1 = r * hsv1[2] * hsv1[1] * math.cos(float(hsv1[0])/1*360 / 180 * math.pi)
    y1 = r * hsv1[2] * hsv1[1] * math.sin(float(hsv1[0])/1*360 / 180 * math.pi)
    z1 = h * (1 - hsv1[2])
    x2 = r * hsv2[2] * hsv2[1] * math.cos(float(hsv2[0])/1*360 / 180 * math.pi)
    y2 = r * hsv2[2] * hsv2[1] * math.sin(float(hsv2[0])/1*360 / 180 * math.pi)
    z2 = h * (1 - hsv2[2])
    dx=x1-x2
    dy=y1-y2
    dz=z1-z2
    return math.sqrt(dx * dx + dy * dy + dz * dz)

hsvRed=hex_to_hsv('#FF0000')
hsvGreen=hex_to_hsv('#008000')
hsvBlue=hex_to_hsv('#0000FF')

def aveDistance(palette):
    RedDis = 0
    GreenDis = 0
    BlueDis = 0
    hsvPalette=rgb_to_hsv_palette(palette)
    for i in hsvPalette:
        RedDis=RedDis+color_distance(i[0],hsvRed)*i[1]
        GreenDis = GreenDis + color_distance(i[0], hsvGreen)*i[1]
        BlueDis = BlueDis + color_distance(i[0], hsvBlue)*i[1]

    print 'red: '
    print RedDis
    print 'green: '
    print GreenDis
    print 'blue: '
    print BlueDis

aveDistance(c1)
aveDistance(c2)
aveDistance(c3)
aveDistance(c4)
aveDistance(c5)
aveDistance(c6)
aveDistance(c7)
aveDistance(c8)
aveDistance(c9)
aveDistance(c10)
aveDistance(c11)
aveDistance(c12)
aveDistance(c13)
aveDistance(c14)
aveDistance(c15)
