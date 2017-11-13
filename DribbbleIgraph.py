import DribbblePlayOffData
import time
import re
import json

def downloadData(playoffID):
    files=[]
    files.append(playoffID)
    DribbblePlayOffData.downloadInfo(playoffID)
    time.sleep(1)
    DribbblePlayOffData.downloadComments(playoffID)
    time.sleep(1)
    rebounds = DribbblePlayOffData.downloadReboundList(playoffID)
    for rebound in rebounds:
        DribbblePlayOffData.downloadInfo(rebound)
        time.sleep(1)
        DribbblePlayOffData.downloadComments(rebound)
        time.sleep(1)
        files.append(rebound)
    return files


def generateCommentsNetwork(ID):
    edges=[]
    infoFile = str(ID)+ '_Info' + '.json'
    commentsFile = str(ID) + '_Comments' + '.json'

    fileInfo = open(infoFile).read()
    infoData = json.loads(fileInfo)
    UserName=infoData['user']['name']

    fileCom = open(commentsFile).read()
    print commentsFile
    ComData = json.loads(fileCom)
    for comment in ComData:
        edge = []
        match = re.findall('>@([A-Za-z0-9\s]+)</a', comment['body'])
        if match == []:
            edge.append(comment['user']['name'])
            edge.append(UserName)
            edge.append('comment')
            edges.append(edge)
        else:
            for i in match:
                print i
                edge = []
                edge.append(comment['user']['name'])
                edge.append(i)
                edge.append('mention')
                edges.append(edge)
    return edges

def Network(playoffID,files):
    outputFile=str(playoffID)+'.csv'
    output = open(outputFile, 'w')
    output.write('from,to\n')
    for file in files:
        edges = generateCommentsNetwork(file)
        if edges!=[]:
            for edge in edges:
                output.write(edge[0].encode('ascii', 'ignore')+','+edge[1].encode('ascii', 'ignore')+','+edge[2]+'\n')


#playOff=DribbblePlayOffData.downloadPlayoffList(1)
#print playOff
#for j in playOff:
#    print j
#    rebound=DribbblePlayOffData.downloadReboundList(j)
#    print rebound

playoffID=3051535
files=downloadData(playoffID)
print files
Network(playoffID,files)

