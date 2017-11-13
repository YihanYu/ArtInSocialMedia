import os
import csv
import numpy as np

disoutput=open('averageDis_activeUsers.csv', 'w')
disoutput.write('user_id,mean,min,max,median,std\n')

for file in os.listdir('/Users/YihanYu/Desktop/ab/result'):
    filename = os.path.basename(file)
    fileHandle = "/Users/YihanYu/Desktop/ab/result" + "//" + filename
    print fileHandle
    dis=[]
#    userID=filename[11:-4]
    userID=filename
    print userID
    with open(fileHandle) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            dis.append(float(line['dis']))
    meanDis=np.mean(dis)
    maxDis=np.amax(dis)
    minDis=np.amin(dis)
    medianDis=np.median(dis)
    stdDis=np.std(dis)
    disoutput.write(userID+','+str(meanDis)+','+str(minDis)+','+str(maxDis)+','+str(medianDis)+','+str(stdDis)+'\n')