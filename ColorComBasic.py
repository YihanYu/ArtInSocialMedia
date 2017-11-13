import colorsys
import matplotlib.colors as colors
import math

R=100.00
angle=30.00
h = R * math.cos(angle / 180 * math.pi)
r = R * math.sin(angle / 180 * math.pi)

c1=['#495C76', '#86A297', '#F8D3AF', '#E18664', '#E1C577', '#FCEECE', '#A9CDC0']
c2=['#775D73', '#F9D3AF', '#D59263', '#8D9F95', '#AACCC0', '#BBC6A8', '#FDF7D9']
c3=['#FFDFB5', '#FFFEFD', '#F7C577', '#FBAA65', '#E55650', '#FFE7C7', '#69B5B9', '#F4DFB8']
c4=['#6A8639', '#FFA56E', '#8CAA46', '#F46450', '#A16E4E', '#CD965B']
c5=['#6E90B2', '#81B2D3', '#F6CE8F', '#FDFDFC', '#D5EBF1', '#52697C', '#DBBA6E']
c6=['#A6BA3D', '#DBE3A3', '#FCFDFD', '#E3E7CE', '#C4B543']
c7=['#FF7E61', '#FFFFFF', '#B1D7FF', '#F8A46E', '#FFE0A7', '#C4A7BF', '#ECD6DC']
c8=['#D8E2EE', '#D9DBA1', '#92ACC4', '#F2F6F9', '#597E8C', '#E9775A', '#CBD3DC']
c10=['#A71414', '#CC4A49']


def hex_to_hsv(hexString):
    RGBValue= colors.hex2color(hexString)
    return colorsys.rgb_to_hsv(RGBValue[0], RGBValue[1], RGBValue[2])

def hex_to_hsv_palette(colorPalette):
    hsvPalette=[]
    for color in colorPalette:
        hsvColor=hex_to_hsv(color)
        hsvPalette.append(hsvColor)
    return hsvPalette

hsvRed=hex_to_hsv('#FF0000')
hsvGreen=hex_to_hsv('#008000')
hsvBlue=hex_to_hsv('#0000FF')


def color_distance(hsv1,hsv2):
    x1 = r * hsv1[2] * hsv1[1] * math.cos(float(hsv1[0])*360 / 180 * math.pi)
    y1 = r * hsv1[2] * hsv1[1] * math.sin(float(hsv1[0])*360 / 180 * math.pi)
    z1 = h * (1 - hsv1[2])
    x2 = r * hsv2[2] * hsv2[1] * math.cos(float(hsv2[0])*360 / 180 * math.pi)
    y2 = r * hsv2[2] * hsv2[1] * math.sin(float(hsv2[0])*360 / 180 * math.pi)
    z2 = h * (1 - hsv2[2])
    dx=x1-x2
    dy=y1-y2
    dz=z1-z2
    return math.sqrt(dx * dx + dy * dy + dz * dz)

def aveDistance(palette):
    RedDis = 0
    GreenDis = 0
    BlueDis = 0
    hsvPalette=hex_to_hsv_palette(palette)
    for i in hsvPalette:
        RedDis=RedDis+color_distance(i,hsvRed)
        GreenDis = GreenDis + color_distance(i, hsvGreen)
        BlueDis = BlueDis + color_distance(i, hsvBlue)
    aveRedDis=RedDis/len(palette)
    aveGreenDis=GreenDis/len(palette)
    aveBlueDis=BlueDis/len(palette)
    print 'red: '
    print aveRedDis
    print 'green: '
    print aveGreenDis
    print 'blue: '
    print aveBlueDis
aveDistance(c1)


#hsvOrange=hex_to_hsv('#ffa500')
#hsvWhite=hex_to_hsv('#ffffff')
#hsvBlack=hex_to_hsv('#000000')
#print color_distance(hsvWhite, hsvBlack)