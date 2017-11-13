import colorsys
import matplotlib.colors as colors
import math
from munkres import Munkres, print_matrix

def hex_to_hsv(hexString):
    RGBValue= colors.hex2color(hexString)
    return colorsys.rgb_to_hsv(RGBValue[0], RGBValue[1], RGBValue[2])

def hex_to_hsv_palette(colorPalette):
    hsvPalette=[]
    for color in colorPalette:
        hsvColor=hex_to_hsv(color)
        hsvPalette.append(hsvColor)
    return hsvPalette

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
c9=['#D9AFC5','#9ABCBB','#D99680','#D3A8A8','#D9D3DF','#9B9A8F']

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

def generate_matrix(colorPalette1, colorPalette2):
    hsvPalette1=colorPalette1
    hsvPalette2=colorPalette2
    len1=len(hsvPalette1)
    len2=len(hsvPalette2)
    matrix=[]
    if len1<len2:
        hsvPalette1,hsvPalette2=hsvPalette2,hsvPalette1
        len1 = len(hsvPalette1)
        len2 = len(hsvPalette2)
    if len1>=len2:
        for i in range(0, len1):
            matrix.append([])
        for j in range(0,len1):
            for k in range(0,len1):
                matrix[j].append(1000000)
        for i in range(0, len1):
            for j in range(0,len2):
                matrix[j][i]=int(round(color_distance(hsvPalette1[i],hsvPalette2[j])*1000))+1
    return matrix

def calculateDis(color1,color2):
    matrix=generate_matrix(color1, color2)

    if abs(len(color1)-len(color2))==0:
        m = Munkres()
        indexes = m.compute(matrix)
#        print_matrix(matrix, msg='Lowest cost through this matrix:')
        total = 0
        for row, column in indexes:
            value = matrix[row][column]
            total += value
#            print '(%d, %d) -> %d' % (row, column, value)
#        print 'total cost: %d' % total
        dis=float(total)/len(color1)/100
        print dis
        return dis

    else:
        gap=abs(len(color1) - len(color2))
#        print gap
        m = Munkres()
        indexes = m.compute(matrix)
#        print_matrix(matrix, msg='Lowest cost through this matrix:')
        total = 0
        columnLeft=[]
        matrixlen=len(indexes)

        for row, column in indexes:
            value = matrix[row][column]
            if value!=1000000:
                total += value
            else:
                columnLeft.append(column)
#            print '(%d, %d) -> %d' % (row, column, value)
#        print columnLeft
        for i in columnLeft:
            leftValue=[]
            for j in range(0,matrixlen-1):
                leftValue.append(matrix[j][i])
#            print leftValue
#            print min(leftValue)
            total += min(leftValue)

#        print 'total cost: %d' % total
        dis=float(total)/matrixlen/100
        print dis
        return dis
