import csv
import itertools
import os
import colorsys
import matplotlib.colors as colors
import math
from munkres import Munkres, print_matrix

fileHandle='/Users/YihanYu/Downloads/30_users_color_palette/3022.csv'

def hex_to_hsv(hexString):
    RGBValue= colors.hex2color(hexString)
    return colorsys.rgb_to_hsv(RGBValue[0], RGBValue[1], RGBValue[2])

def hex_to_hsv_palette(colorPalette):
    hsvPalette=[]
    for color in colorPalette:
        hsvColor=hex_to_hsv(color)
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
    combl = combList(fileDir)
    outputFile='dis_'+os.path.basename(fileDir)
    output=open(outputFile, 'w')
    output.write('shot1_id,shot1_createdTime,shot1_colorPalette,shot2_id,shot2_createdTime,shot2_colorPalette\n')
    for j in combl:
        with open(fileDir) as csvf:
            reader = csv.DictReader(csvf)
            for i, rows in enumerate(reader):
                if i == j[0]:
                    color='"'+str(hex_to_hsv_palette(eval(rows['color'])))+'"'
                    output.write(rows['id']+','+rows['created_time']+','+color+',')
                if i == j[1]:
                    color = '"' + str(hex_to_hsv_palette(eval(rows['color']))) + '"'
                    output.write(rows['id'] + ',' + rows['created_time'] + ',' + color + '\n')

for file in os.listdir('/Users/YihanYu/Desktop/ab/raw'):
    fileHandle = "/Users/YihanYu/Desktop/ab/raw" + "//" + file
    colorComb(fileHandle)

#fileHandle='/Users/YihanYu/Desktop/color_dis/821264_before.csv'

#colorComb(fileHandle)