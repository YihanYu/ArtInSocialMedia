import csv
import os
import re
import nltk
from nltk import FreqDist
from nltk.collections import*

fileDir='/Users/YihanYu/Desktop/Twitter_Sam/days2017-7-12tweets.csv'
terms = 'GunOwners,National Shooting Sports Foundation,NSSF,GOA,Gun Owners of America,National Rifle Association,2AF,SethWaugh,2AFDN,CalgunsFdn,hellerrkba,Heller Foundation,FloridaCarryInc,Florida Carry,FL_Open_Carry,Florida Open Carry,USCCA,georgiacarry,Georgia Carry,jpfo,real_jpfo,jpfoalert,jfpo_liberty,Jews for the Preservation of Firearms Ownership,liberalgunclub,liberal gun club,nagr,natlgunrights,National Association for Gun Rights,VCDL,VCDL_Org,Virginia Citizens Defense League,guntruth,The Truth About Guns,concealedcampus,concealedCT,concealedDE,ConcealedNEast,ConcealedVT,ConcealedNJ,ConcealedNY,ConcealedMA,ConcealedME,ConcealedRI,ConcealedNH,ConcealedNE,ConcealedMN,ConcealedKS,ConcealedND,ConcealedCentrl,ConcealedIA,ConcealedSD,ConcealedMO,SCCC,CCRKBArms,Citizens Committee for the Right to Keep and Bear Arms,rkba,RMGunOwners,Rocky Mountain Gun Owners,Pnkpistol,Pink Pistols,PinkPistolsTBay,PinkPistolsOKLA,PinkPistolsSoFl,pinkpistolstc,pinkpistolsabq,pinkpistols_OAK,pinkpistolsrva,ASRPA,Arizona State Rifle and Pistol Association,EVERYT0WN,national reciprocity,resp_solutions,Americans for Responsible Solutions,smartgunlaws,Law Center to Prevent Gun Violence,EFSGV,CSGV,Coalition to Stop Gun Violence,AMWAGVTF,CAPActionGuns,VoteGunSafety,ProtectMN,MomsDemand,EndGunViolence,ASLGVP,GPacIllinois,GPac,NYLGVP,Bradybuzz,Brady Campaign,BradyCenter,Brady Center,FLCoPreventGV,PrevGunViolence,sbcoalition,CAGV,CJRC,Everytown,MomsDemand,WeAreDoneAsking,GunVictimsAct,open carry,concealed carry reciprocity,concealed carry,molon labe,ccw,constitutional carry,2A,gun control,assault weapons,NRA,NRATV,NRAILA,NRAblog,NRA_Rifleman,NRAPVF,CNYFNRA,NraWayne'
terms=terms.split(',')
terms.append(',')
stopwords=nltk.corpus.stopwords.words('english')+terms

bigram_measures=nltk.collocations.BigramAssocMeasures()


def hashtagFrequency(fileDir):
    outputFile='hashtag_'+os.path.basename(fileDir)
    output=open(outputFile, 'w')
    output.write('hashtag,fre\n')

    with open(fileDir) as csvfile:
        allhashtags=[]
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['hashtags'] !='':
                tags=line['hashtags']
                tags=tags.split(',')
                for tag in tags:
                    allhashtags.append(tag)
    hashtag=set(allhashtags)
    for i in hashtag:
        fre=allhashtags.count(i)
        output.write(i+','+str(fre)+'\n')

def mentionFrequency(fileDir):
    outputFile='mention_'+os.path.basename(fileDir)
    output=open(outputFile, 'w')
    output.write('mention,fre\n')

    with open(fileDir) as csvfile:
        allmentions=[]
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line['user_mentions'] !='':
                mentions=line['user_mentions']
                mentions=mentions.split(',')
                for mention in mentions:
                    allmentions.append(mention)
    mention=set(allmentions)
    for i in mention:
        fre=allmentions.count(i)
        output.write(i+','+str(fre)+'\n')

def termFrequency(fileDir):
    outputFile1='term_'+os.path.basename(fileDir)
    output1=open(outputFile1, 'w')
    output1.write('term,fre\n')

    outputFile2 = 'unigram_' + os.path.basename(fileDir)
    output2 = open(outputFile2, 'w')
    output2.write('term,fre\n')

    outputFile3 = 'bigram_' + os.path.basename(fileDir)
    output3 = open(outputFile3, 'w')
    output3.write('term1,term2,score\n')

    with open(fileDir) as csvfile:
 #       text=''
 #       reader = csv.DictReader(csvfile)
 #       for line in reader:
 #           if line['message'] !='':
 #               text=text+line['message'].decode('utf-8')+' '

        reader = csv.reader(csvfile)
        column = [row[3].decode('utf8', 'ignore') for row in reader]
        text= ' '.join(column)
        text = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", text)

        for term in terms:
            count=len(re.findall(term, text, flags=re.IGNORECASE))
            output1.write(term+','+str(count)+'\n')


        texttokens=nltk.word_tokenize(text)
        textwords=[w.lower() for w in texttokens if not w in stopwords]
        fredist=FreqDist(textwords)
        for word in fredist.keys():
            print word, fredist[word]
            wordstring='"'+word.strip().encode('utf-8')+'"'
            output2.write(wordstring + ',' + str(fredist[word]) + '\n')


        finder=nltk.collocations.BigramCollocationFinder.from_words(textwords)
        scored=finder.score_ngrams(bigram_measures.raw_freq)
        for j in scored:
            word1='"'+j[0][0].strip().encode('utf-8')+'"'
            word2='"'+j[0][1].strip().encode('utf-8')+'"'
            output3.write(word1+','+word2 + ',' + str(j[1]) + '\n')

for file in os.listdir('/Users/YihanYu/Desktop/Twitter_Sam'):
    fileDir = "/Users/YihanYu/Desktop/Twitter_Sam" + "//" + file
    print fileDir
    hashtagFrequency(fileDir)
    mentionFrequency(fileDir)
    termFrequency(fileDir)