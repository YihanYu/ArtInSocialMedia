import os
import csv
import googleAPI

for file in os.listdir('/Users/YihanYu/Downloads//top30users'):
    filename = os.path.basename(file)
    print filename
    fileHandle = "/Users/YihanYu/Downloads//top30users" + "//" + filename
    outFile = 'color_' + filename
    output = open(outFile, 'w')
    output.write('id, created_time, link, color_plate, color_count\n')
    with open(fileHandle) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            print line['id']
            color=googleAPI.googleAPI(line['link'])
            colorLengh=len(color)
            color='"'+str(color)+'"'
            output.write(str(line['id'])+','+str(line['created_time'])+','+str(line['link'])+','+color+','+str(colorLengh)+'\n')
