import os
import csv

freoutput=open('playoffsFre.csv', 'w')
freoutput.write('user_id,frequency\n')

allUsers=[]
user=[]
for file in os.listdir('/Users/YihanYu/Downloads/playoffs/rebounds'):
    filename = os.path.basename(file)
    fileHandle = "/Users/YihanYu/Downloads/playoffs/rebounds" + "//" + filename
    print fileHandle
    with open(fileHandle) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            print line['user_id']
            allUsers.append(line['user_id'])

user=set(allUsers)
for i in user:
    fre=allUsers.count(i)
    freoutput.write(i + ',' + str(fre) + '\n')