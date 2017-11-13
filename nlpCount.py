import os
import csv

output=open('unigram_all.csv', 'w')
output.write('term,fre\n')

for file in os.listdir('/Users/YihanYu/Desktop/RevisedTermFreResults/resultsByDay/unigram'):
    filename = os.path.basename(file)
    fileHandle = "/Users/YihanYu/Desktop/RevisedTermFreResults/resultsByDay/unigram" + "//" + filename
    fredict = {}
    print fileHandle
    with open(fileHandle) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            word=line['term']
            if line['fre']!='':
                count=int(line['fre'])
                if word in fredict:
                    fredict[word]+=count
                else:
                    fredict[word]=count
for i in fredict.keys():
    j=str(fredict[i])
    i = '"' + i + '"'
    output.write(i+','+j+'\n')