from numpy import *
import colorsys
import matplotlib.colors as colors
import math
from munkres import Munkres, print_matrix

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


def hex_to_hsv(hexString):
    RGBValue= colors.hex2color(hexString)
    return colorsys.rgb_to_hsv(RGBValue[0], RGBValue[1], RGBValue[2])

def hex_to_hsv_palette(colorPalette):
    hsvPalette=[]
    for color in colorPalette:
        hsvColor=hex_to_hsv(color)
        hsvPalette.append(hsvColor)
    return hsvPalette


def color_distance(hsv1,hsv2):
    x1 = r * hsv1[2] * hsv1[1] * math.cos(float(hsv1[0]) / 180 * math.pi)
    y1 = r * hsv1[2] * hsv1[1] * math.sin(float(hsv1[0]) / 180 * math.pi)
    z1 = h * (1 - hsv1[2])
    x2 = r * hsv2[2] * hsv2[1] * math.cos(float(hsv2[0]) / 180 * math.pi)
    y2 = r * hsv2[2] * hsv2[1] * math.sin(float(hsv2[0]) / 180 * math.pi)
    z2 = h * (1 - hsv2[2])
    dx=x1-x2
    dy=y1-y2
    dz=z1-z2
    return math.sqrt(dx * dx + dy * dy + dz * dz)

def generate_matrix(colorPalette1, colorPalette2):
    hsvPalette1=hex_to_hsv_palette(colorPalette1)
    hsvPalette2=hex_to_hsv_palette(colorPalette2)
    len1=len(hsvPalette1)
    len2=len(hsvPalette2)
    if len1>=len2:
        matrix = mat(zeros((len1, len1)))
        for i in range(0, len1):
            for j in range(0, len1):
                matrix[i, j] = 1000000
        for i in range(0, len1):
            for j in range(0,len2):
                matrix[j, i]=round(color_distance(hsvPalette1[i],hsvPalette2[j])*1000)
    return matrix

Matrix=generate_matrix(c1, c4)
print Matrix
a=[]
for i in range(0,5):
    a.append([])
print a[3]




