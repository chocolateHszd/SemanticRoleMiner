#Goal : For each sentence args for a root are investigated


def findPreds(sentence):
    preds={}
    #print sentence
    #print senna.keys()
    counter=0
    for senKey,senVal in sentence.items():
        token=senVal.keys()
        cols=senVal.values()
	cols=cols[0]
        #print cols
        tok_keys=cols.keys()
        tok_tags=cols.values()
        for col, tag in cols.items():
            if tag[-1]=="V" :
               preds[counter]=[]
               preds[counter].append(token)
               preds[counter].append(str(col))
               counter+=1
    return preds
#-----------------------------------------------------------------

def findDomain(args):

    elements= args.values()
    #print elements
    domains={}
    for key,val in args.items():
        first=val[0][0]
        first=first.split("-")
        first=first[1]
        #print first
        last=val[-1][0]
        last=last.split("-")
        last=last[1]
        #print last
        domains[key]=[]
        domains[key].append(first)
        domains[key].append(last)
    return domains    
   
#------------------------------------------------------------------

def findArg(verb,targetDict,targetCol):
    
     tokenLabels={}
     Labels={}
    #---Testing function arguments Perfect working
     #print verb
     #print targetDict
     root=verb.split("-")
     index=root[1]
     root=root[0]
     

     #--Finding the target column for retreiving correct args
     targetColumn='Null'
     for element_id in targetDict[int(index)][str(verb)]:
         #print element_id
         #print targetDict[int(index)]["reported-17"][element_id]
         take=targetDict[int(index)][str(verb)][element_id]   
         if take[-1]=="V":
            #print element_id
            targetColumn=element_id
     

     #--having all args for all tokens  
     for item in targetDict.values():
         val=item.values()
         token=item.keys()
         #print token
	 val=val[0]
	 #print "bol"+str(targetColumn)
         
         arg=val[int(targetCol)]
	 if arg!="O":
	 	arg=arg.split("-")
                if arg[1]=="AM":
                  arg=arg[1]+"-"+arg[2]
		else:         	
		  arg=arg[1]
		myArg=arg+"-"+root
		#print myArg 
		if myArg in tokenLabels:
		   tokenLabels[myArg].append(token)
		else:
		   tokenLabels[myArg]=[]
		   tokenLabels[myArg].append(token) 
		  
     #tokenLabels['Tanks']='A0'
     return tokenLabels

#-------------------------------------------------------------------------------------------

def findParts(targetTuple,AR,root):
    newAR=""
    #print "targettuple"+str(targetTuple)
    dep=targetTuple[0]
    part1=targetTuple[1]
    #print "dep"+str(dep)
    sw1=0
    sw2=0
    part2=targetTuple[2]
    #print part1, part2
    #print AR
    verbconnection=0
    for arg in AR:
       newAR=""
       
       for tup in AR[arg]:
          
           if tup[0]==part1[0] and str(tup[1])==part1[1]: #finding first match
               sw1=1 
               #print arg, arg[0]
               #print tup[0]
	       if arg[0]=="V":
                  verbconnection=1
                  #print "1"
                  #print "hi"
		  #newAR="V-"+str(root)
           elif tup[0]==part2[0] and str(tup[1])==part2[1]: #finding second match
               sw2=1
               #print  arg, arg[0]
               #print tup[0]
               if arg[0]=="V":
                  verbconnection=1
                  #print "1"
		  #newAR="V-"str(root)
           if sw1==1 and sw2==1:
	       break # good point to break out of loop as the first matching case is found

       if sw1==1 and sw2==1 : # means 2 parts are found
           #print arg, part1, part2       #             A1   ['debris', '11'] ['contamination', '17']
           #print dep, arg, part1 , part2 #  conj_and   A1   ['debris', '11'] ['contamination', '17']
           #print verbconnection  
	   if verbconnection==1: 
               newAR="Link-"+str(root)
           else :
               newAR=arg
           #print part1
	  
	   break
    return newAR
#-----------------------------------------------------------
def mixDepArg(ST,AR, verb):
     mixDict={}
     counter=0
     switch=0
     take_arg=[]
     temp=[]
     plainverb=verb.split("-")
     plainverb=plainverb[0]
     verb1=[] # modifying the proper format for verb
     verb1.append(verb)
     verb=verb1
     #print verb
     #print "ST"+str(ST)
     #print "AR"+str(AR)
     #print "---------------"
     for val in ST.values():
       #print val
       
       dep=val.keys()
       dep=dep[0]
       tokens=val.values()
       tokens=tokens[0]
       part1=[]
       part1.append(tokens[0])
       part2=[]
       part2.append(tokens[1])
       #print dep,part1,part2
       for ar,value in AR.items():
           #print ar
           if part1 in value and part2 in value: # having both parts of dependency 
              #print value
	      d={}
              d[dep]=(part1,part2)
              #print d
              a={}
              a[ar]=d
              mixDict[counter]=a
              counter+=1
	   elif (part2 in value and part1==verb) or (part1 in value and part2==verb):  # I want to label these types of dependencies as a link from verb to the token "Link-verb" 
              #print "hi"
              #print ar
              d={}
              d[dep]=(part1,part2)
              #print d
              a={}
              a["Link-"+plainverb]=d
              mixDict[counter]=a
              counter+=1
           elif ((part1 in value and part2 not in value)or(part2 in value and part1 not in value) )and (part1!=verb and part2!=verb):
              #print part1,part2, ar
              
              take_arg.append(ar)
	      switch+=1
              if switch==2 :
                 #ar="Link-"+str(ar[0])+str(ar[1])
                 d={}
                 d[dep]=(part1,part2)
                 #print d
                 a={}
                 #print "Link-"+str(take_arg[0])+"-"+str(take_arg[1])
                 a["Link-"+str(take_arg[0])+"-"+str(take_arg[1])]=d
                 mixDict[counter]=a
                 counter+=1
                 
           
     if mixDict!="Null":
        return mixDict       

#------------------------------------------
def Find_Pred_Arg_Root(myTestFile,SEN0_SE,SEN0_ST):
   root=myTestFile.findRoot(SEN0_ST)
   allPreds=findPreds(SEN0_SE)


   #---- testing predicates ------------
   i=1 # 0 is reserved for root
   PRED={}
   ARGS={}
   for item in allPreds.values():
       verb=item[0][0]
       col=item[1]
       if verb==root: #---if the verb is root then it takes 0 index 
          PRED[0]=verb
          ARGS[0]=findArg(root,SEN0_SE,col)
       else:
          PRED[i]=verb
          ARGS[i]=findArg(verb,SEN0_SE,col)
          i+=1 
   return(PRED,ARGS,root)

#-----------------------------------------------
def Find_ArgDom_MixArgDep(ARGS,PRED,SEN0_ST):
   ARGDOM={} 
   MIXARGS={}
   for key,val in ARGS.items():
       ARGDOM[key]=findDomain(val)
       MIXARGS[key]=mixDepArg(SEN0_ST,ARGS[key],PRED[key])
   return (ARGDOM,MIXARGS)




