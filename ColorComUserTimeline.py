import csv
import itertools
import colorsys
import matplotlib.colors as colors
import math
from munkres import Munkres, print_matrix

R=100.00
angle=30.00
h = R * math.cos(angle / 180 * math.pi)
r = R * math.sin(angle / 180 * math.pi)

fileHandle='/Users/YihanYu/PycharmProjects/ArtStation/color_628711.csv'

def rgb_to_hsv_palette(colorPalette):
    hsvPalette=[]
    for rgbw in colorPalette:
        hsv = colorsys.rgb_to_hsv(float(rgbw[0])/255, float(rgbw[1])/255, float(rgbw[2])/255)
        hsvColor=[]
        hsvColor.append(hsv)
        hsvColor.append(rgbw[3])
        hsvPalette.append(hsvColor)
    return hsvPalette


def combList(fileDir):
    with open(fileDir) as csvfile:
        lenreader = csv.DictReader(csvfile)
        lenList=[0]
        lent=0
        for line in lenreader:
            lent=lent+1
            lenList.append(lent)
        lenList=lenList[:-1]
        combList=list(itertools.combinations(lenList, 2))
        print len(combList)
    return combList

def colorComb(fileDir):
    colorComb=[]
    combl = combList(fileDir)
    for j in combl:
        com=[]
        with open(fileDir) as csvf:
            reader = csv.DictReader(csvf)
            for i, rows in enumerate(reader):
                if i == j[0]:
                    hsvcolor=rgb_to_hsv_palette(eval(rows[' color_plate']))
                    com.append(hsvcolor)
                if i == j[1]:
                    hsvcolor = rgb_to_hsv_palette(eval(rows[' color_plate']))
                    com.append(hsvcolor)
        colorComb.append(com)
    return colorComb

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

def generate_matrix(colorPalette1, colorPalette2):
    len1=len(colorPalette1)
    len2=len(colorPalette2)
    matrix=[]
    if len1>=len2:
        for i in range(0, len1):
            matrix.append([])
        for j in range(0,len1):
            for k in range(0,len1):
                matrix[j].append(100000)
        for i in range(0, len1):
            for j in range(0,len2):
                matrix[j][i]=int(round(color_distance(colorPalette1[i][0],colorPalette2[j][0])*10))+1
    m = Munkres()
    indexes = m.compute(matrix)
    print indexes
    print_matrix(matrix, msg='Lowest cost through this matrix:')
    total = 0
    for row, column in indexes:
        value = (colorPalette1[row][1]+colorPalette2[column][1])/float(matrix[row][column])*1000000
        total += value
        print '(%d, %d) -> %d' % (row, column, value)
    print 'total cost: %d' % total


test=colorComb(fileHandle)[6]
matrix=generate_matrix(test[0], test[1])
