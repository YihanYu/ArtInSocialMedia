import csv
import os
import colorsys
import matplotlib.colors as colors

fileHandle1='/Users/YihanYu/Downloads/30_users_color_palette/3022.csv'
fileHandle2=''

def hex_to_hsv(hexString):
    RGBValue= colors.hex2color(hexString)
    return colorsys.rgb_to_hsv(RGBValue[0], RGBValue[1], RGBValue[2])

def hex_to_hsv_palette(colorPalette):
    hsvPalette=[]
    for color in colorPalette:
        hsvColor=hex_to_hsv(color)
        hsvPalette.append(hsvColor)
    return hsvPalette

def colorComb(fileDir1,fileDir2):
    outputFile='dis_'+os.path.basename(fileDir1)
    output=open(outputFile, 'w')
    output.write('shot1_id,shot1_createdTime,shot1_colorPalette,shot2_id,shot2_createdTime,shot2_colorPalette\n')
    with open(fileDir1) as csvf:
        reader = csv.DictReader(csvf)
        for line in reader:
            with open(fileDir2) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    color = '"' + str(hex_to_hsv_palette(eval(line['color']))) + '"'
                    output.write(line['id'] + ',' + line['created_time'] + ',' + color + ',')
                    color = '"' + str(hex_to_hsv_palette(eval(row['color']))) + '"'
                    output.write(row['id'] + ',' + row['created_time'] + ',' + color + '\n')

fileHandle1='/Users/YihanYu/Desktop/ab/raw/a.csv'
fileHandle2='/Users/YihanYu/Desktop/ab/raw/b.csv'
fileHandle3='/Users/YihanYu/Desktop/color_dis/821264_rebounds.csv'
colorComb(fileHandle2,fileHandle1)