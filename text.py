import DribbblePlayOffData
import csv
import re
import json

def downloadData(playoffID):
    files=[]
    files.append(playoffID)
    DribbblePlayOffData.downloadInfo(playoffID)
    DribbblePlayOffData.downloadComments(playoffID)
    rebounds = DribbblePlayOffData.downloadReboundList(playoffID)
    for rebound in rebounds:
        DribbblePlayOffData.downloadInfo(rebound)
        DribbblePlayOffData.downloadComments(rebound)
        files.append(rebound)
    return files

def generateCommentsNetwork(ID):
    edges=[]
    infoFile = str(ID)+ '_Info' + '.json'
    commentsFile = str(ID) + '_Comments' + '.json'

    fileInfo = open(infoFile).read()
    infoData = json.loads(fileInfo)
    UserName=infoData['user']['username'].encode('ascii','replace')

    fileCom = open(commentsFile).read()
    print commentsFile
    ComData = json.loads(fileCom)
    for comment in ComData:
        edge = []
        match = re.findall('@([A-Za-z0-9\s]+)', comment['body'])
        if match == []:
            edge.append(comment['user']['name'].encode('ascii','replace'))
            edge.append(UserName)
            edges.append(edge)
        else:
            for i in match:
                edge = []
                edge.append(comment['user']['name'].encode('ascii', 'replace'))
                edge.append(i.encode('ascii', 'replace'))
                edges.append(edge)
    return edges

playoffID=3088002

files=downloadData(playoffID)
print files
generateCommentsNetwork(3088002)
print files