#preprocessing senna file
def modifySenna(inputFile):
         
	j=0
        #print inputFile			   
	dummyfile=open(inputFile,'r')
	sennaIterator=dummyfile.read()
        sentences_Senna={}
        tokenloc=0
	sentences_Senna["sen0"]={}
	for line in sennaIterator.split("\n"):
	   tokens=line.replace(" ","")
	   tokens=tokens.replace("\t","|")
	   tokens=tokens.split("|")
	   #print tokens
           tokenloc+=1
	   if tokens[0]!=".": 
		counter=1
		sentences_Senna["sen"+str(j)][tokenloc]={}
                sentences_Senna["sen"+str(j)][tokenloc][tokens[0]]={}
		for element in tokens[1:]:
		    #print element
		    sentences_Senna["sen"+str(j)][tokenloc][tokens[0]][counter]=element

		    counter+=1
	   else: 
	     j+=1 
	     #print "end"
	     tokenloc=0
	     sentences_Senna["sen"+str(j)]={}
	      
		#print sentences_Senna["sen0"]["Tanks"]
		#print sentences_Senna["sen0"]["used"]
		#print sentences_Senna["sen1"]["Sand"]
        return sentences_Senna
	# outputs of senna proccess
	# 2 sentences are identified sentences_senna{"sen0"={"Tanks"={"0"=NNS,...},"used"={"0"=VBN,...}}, "sen1"={"Sand"={...},"and"={}, "activated={}"}}
	#sentences_Senna["sen0"]["Tanks"] => {0: 'NNS', 1: 'S-NP', 2: 'O', 3: '-', 4: 'S-A0', 5: 'B-A0', 6: '(S1(S(NP(NP*)'}
	#sentences_Senna["sen0"]["used"]  => {0: 'VBN', 1: 'S-VP', 2: 'O', 3: 'used', 4: 'S-V', 5: 'I-A0', 6: '(VP*'}
	#sentences_Senna["sen1"]["Sand"]  => {0: 'NN', 1: 'S-NP', 2: 'S-PER', 3: '-', 4: 'O', 5: 'O', 6: 'B-A1', 7: 'O', 8: 'O', 9: '(S1(S(NP*)'}

