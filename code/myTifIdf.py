import sys
import os
import en
from stemming.porter2 import stem
from math import *

def remStopWords(inputDic):
	stoplist=[]
	stoplist=(open("/home/kimia/srl/python/SemanticRoleMiner/code/stopwords.txt","r")).read().split(",")
	stoplist=stoplist[:-1] #last item removed from stoplist
	#print stoplist
	for word in stoplist:
		if word in inputDic.keys():
			del inputDic[word]

def TfIdf(countDic,countAll,total):
	allCalcs={}
	for word,value in countDic.items():
		temp=float(value)/total
		allCalcs[word]=100*temp*countAll[word]
		#print temp, word
	return allCalcs


def CountDoc(newFile,countDic,countAll):
	cD={}
	cA={}
	cD=countDic
	cA=countAll
	tokens=newFile.keys()
	values=newFile.values()
	#print countDic
	for item in tokens:
		if item in countDic:
			#print item
			cD[item]+=1
			#print item, cA[item] , newFile[item]
			if cA[item]<newFile[item]: cA[item]=newFile[item]
		else: 
			cD[item]=1
			cA[item]=newFile[item]
	return cD,cA

def docDic(inputFile):
	inputDic={}
	getText=inputFile.read()
	getText=getText.replace("\n","")
	symlist=["(",")",";",":",",","/","-","_","+","=","[","]","{","}","*","&","%","$","#","@","!","~",".","?","<",">","`"]
	for item in symlist: getText=getText.replace(item,"")
	numlist=["1","2","3","4","5","6","7","8","9","0"]
	for item in numlist: getText=getText.replace(item,"")
	getText=getText.strip(',.').lower()
	textList=[]
	textList=getText.split(" ")
	for x in textList[:]:
		if len(x) < 4 : textList.remove(x)
	for x in textList[:]:
		x=en.noun.singular(x)
		x=stem(x)
		x=en.spelling.suggest(x)[0]
		if x in inputDic:
			inputDic[x]+=1
		else:
			inputDic[x]=1
	vals=max(inputDic.values()) #normalizing
	for key,val in inputDic.items():
		inputDic[key]=float(val)/vals
	#print vals
	return inputDic
countDic={}
countAll={}
#inputF1=open("/home/kimia/srl/python/SemanticRoleMiner/code/input1.txt","r")
#inputF2=open("/home/kimia/srl/python/SemanticRoleMiner/code/input2.txt","r")

inputF1=open("/home/kimia/srl/python/SemanticRoleMiner/code/promed1.txt","r")
in1= docDic(inputF1)
inputF2=open("/home/kimia/srl/python/SemanticRoleMiner/code/promed2.txt","r")
in2= docDic(inputF2)
inputF3=open("/home/kimia/srl/python/SemanticRoleMiner/code/promed3.txt","r")
in3= docDic(inputF3)

inputF1.close()
inputF2.close()
inputF3.close()



totalNumberOfDoc=3
[countDic,countAll]=CountDoc(in1,countDic,countAll)
#print "Cd ",countDic
#print "Ca ",countAll

#print in2
[countDic,countAll]=CountDoc(in2,countDic,countAll)
#print "Cd ",countDic #tested
#print "Ca ",countAll #tested

[countDic,countAll]=CountDoc(in3,countDic,countAll)
#print "Cd ",countDic #tested
#print "Ca ",countAll #tested

takeTFs={}
takeTfs=TfIdf(countDic,countAll,totalNumberOfDoc)
remStopWords(takeTfs) # tested , stop words removed

resultFile=open("/home/kimia/srl/python/SemanticRoleMiner/code/TFresults.txt","w")
for word, val in takeTfs.items():
	resultFile.write("actual Word: "+word+" | value: "+str(val)+"  |  Highest Freq: "+ str(countAll[word])+" | Repeated in: "+str(countDic[word])+" documents \n------------------------------------------------------------------------------------\n")
	if val>20:
		print word,"-",val

resultFile.close()




