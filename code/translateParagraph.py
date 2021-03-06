import os
import sys
path="/home/kimia/srl/"
paragName="/Allabs/abstract"
#initialization
paragraphNumber=open("/home/kimia/srl/SemanticRoleMiner/code/input/paragNumber.txt","r")
pNumber=str(paragraphNumber.readline())
#pNumber="4"
paragraphNumber.close()
if "\n" in pNumber: pNumber=pNumber.replace("\n","")

outputFile=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/Allresult.txt","w")
outputFile.close()
evalFile=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/Allevals.txt","w")
evalFile.close()
ttlFile=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/Allresult.ttl","w")
ttlFile.close()
SennaStan=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/Stan_Senna_results.txt",'w')
SennaStan.close()

abbreviationFile=open(path+"SemanticRoleMiner/code/input/abbreviation.txt","w")
abbreviationFile.close()
count=1

temp=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/test_input.txt","r")
txt=temp.read()
txt=txt.replace(". ",".\n")
txt=txt.replace("; "," .\n")
print txt


counter=0
for line in txt.split("\n"):
	#print count
	print line
	counter+=1
	if len(line)>1:
		inputFile=open(path+"SemanticRoleMiner/code/input/test_input.txt","w")
		inputFile.write(line)
		initfile=open(path+"SemanticRoleMiner/code/input/init.txt","w")
		initfile.write(str(counter))
		initfile.close()
		inputFile.close()
		print line
		abbrv=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/abbreviation.txt","r") #openning abb file
		abb=abbrv.read()
		abbreviationFile=open(path+"SemanticRoleMiner/code/input/abbreviation.txt","w")
		abbreviationFile.write(abb)
		abbreviationFile.close()
		abbrv.close()
		cmd=os.system('python /home/kimia/srl/SemanticRoleMiner/code/main.py')
		print "---000--------0000--------0000"
		result=open(path+"SemanticRoleMiner/code/input/results.txt","r") # results for 1 sentence
		getall=result.read()
		 
		
		#print getall
		outputFile=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/Allresult.txt","a")
		outputFile.write("Sentence: "+str(count)+"\n"+"*********************************************\n")
		#outputFile.write(line)
		outputFile.write(getall+"\n")
		outputFile.close()

		ss=open(path+"SemanticRoleMiner/code/input/Stan_Senna_results.txt",'r')
		getall=ss.read()
		SennaStan=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/Stan_Senna_results.txt",'a')
		SennaStan.write("Sentence: "+str(count)+"\n"+"*********************************************\n")
		SennaStan.write(getall+"\n")
		SennaStan.close()
		ss.close()

		gg=open(path+"SemanticRoleMiner/code/input/gephi.dot","r")
		getall=gg.read()
		gephi=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/gephi"+str(count)+".dot","w")
		gephi.write(getall)
		gephi.close()
		gg.close()

		evalFile=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/Allevals.txt","a")
		evaloutput=open(path+"SemanticRoleMiner/code/input/eval_result.txt","r") # so for each sentence I have 1 result
		getEvals=evaloutput.read()
		evalFile.write(getEvals+"\n")
		evalFile.close()
		evaloutput.close()

		ttlFile=open(path+"SemanticRoleMiner/code"+paragName+pNumber+"/Allresult.ttl","a")
		ttlOutput=open(path+"SemanticRoleMiner/code/input/rdf.ttl","r")
		getTtl=ttlOutput.read()
		print "\n\n****************TTLTTLTTL",getTtl
		ttlFile.write(getTtl+"-------------------------------------------------\n")
		ttlFile.close()
		ttlOutput.close()

		count+=1
