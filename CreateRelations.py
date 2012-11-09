

#triples_file=open("~/srl")
def s_P_o(token2,rel,token1):
    
    print str(token2)+rel+str(token1)



def mainArg(token,mixedArgs):
    elements=mixedArgs.values()
    for temp in elements:
        if len(temp)!=0:
	   arg=temp.keys()[0]
           value=temp.values()
	   value=value[0]
           #print value 
           value=value.values()
           #print value[0][0]
           if token in value[0] and arg!="V":
              print (token,"is",arg)
              break
           
           #if part1==token or part2==token:
              #print token, arg
    print "----"



#-- Check if verb is negate or not
def checkNegate(verb,mixedArgs):
     elements = mixedArgs.values()
     neg=""
     #print elements
     #print "---"
     for temp in elements:
        if len(temp)!=0 and temp.keys()[0]=="V":
          value=temp.values()
          #print value[0].keys()
          if value[0].keys()[0]=="neg":
              neg="not"
              break
    # print arg
     return neg
     #print "----------------"

#-- Find direct Object for a given verb. these types of verbs usually have nsubj
def findObj(verb,mixedArgs):
    obj=[]
    elements= mixedArgs.values()
    for temp in elements:
        if len(temp)!=0 :
	   value=temp.values()
           value=value[0]           
           rel=value.keys()
           #print rel
           value=value.values()
           if verb in value[0] and rel[0]=="dobj":
              obj.append(value[0][1])
              
    return obj          

#-- Find hidden relations 

def inRel(token,mixedArgs):
    sbj=[]
    sbj.append(token)
    elements=mixedArgs.values()
    #find prep
    for temp in elements:
        #print temp
        if len(temp)!=0:
           value=temp.values()
           arg= temp.keys()
           arg=arg[0]
           value=value[0]
	   #print arg
           rel=value.keys()
           val=value.values()
           val=val[0]
           rel=rel[0]
           rel=rel.split("_")
	   #print rel[0]
	   #print val[0]
           if rel[0]=='prep' and val[0]==token:
              sbj.append(rel[1])
              sbj.append(val[1])
           

    return sbj


#-- I first extracted arg, rel, token1 and token2

def makeRel(mixedArgs):
    for elements in mixedArgs.values():
      #print elements #returns a dict
      negate=" " # this is my negate switch to recog verb 
      arg=elements.keys()
      #print arg
      if len(arg)!=0:
         arg=arg[0]
         #print "arg:"+str(arg)
         elements=elements[arg] # returns a list of dependency rel
         #print rel
         rel=elements.keys()
         rel=rel[0]
         #print rel   #relation retirieved
         elements=elements[rel] #a tuple of 2 tokens
         token1=elements[0]
         token2=elements[1]
         print token1 #each token along with their location
         print token2 
 
         if arg=="Link":
		#-- token1 is verb ; hence should be checked if it's negative or positive
		negate= checkNegate(token1,mixedArgs)
		if rel=="nsubjpass": #this relation makes token2 as main nsubject 
                       # sbj=inRel(token2,)    
		 	s_P_o(token2,"is"+negate,token1)
			#mainArg(token2,mixedArgs)
                elif rel=="nsubj":  #this relation takes verb as the name of relation and I need to search for object of the verb
                        obj=findObj(token1,mixedArgs)
                        for item in obj:
			   s_P_o(token2,str(negate)+str(token1),item)
                           mainArg(item,mixedArgs)
                        mainArg(token2,mixedArgs)
                        
         elif rel=="nn" or rel=="amod":
                s_P_o(token1,"is",token2)


#------------
# making St0-verb
def makeSt0(Args):
    verb="Not Found"
    Arg0="No-Arg0"
    Arg1="No-Arg1"
    for key,val in Args.items():
        #print key
        #print val
        #print key[0:2]
        # I just need the keys for now
        if key[0]=="V":
           key=key.replace("V-","")
           verb=key
           #print "verb is "+str(key)
        elif key[0:2]=="A0":
           Arg0="Arg0"
        elif key[0:2]=="A1":
           Arg1="Arg1"  
    
    Arg0=Arg0+"-"+str(verb)
    Arg1=Arg1+"-"+str(verb)
    return str(Arg0)+" "+str(verb)+" "+str(Arg1)
         
def makeSt1(Args):
   #seeking for Arg2
   Arg2=""
   depFound=""
   verb=""
   target=""
   listArg=[]
   listLink=[]
   vals=Args.values()
   for item in vals: 
	#print item
        arg=item.keys()
        arg=arg[0]
        dep=item.values()
        dep=dep[0]
        #dep=dep[0].keys()[0]
        if arg[0:2]=="A2":
           Arg2="A2"
           verb=arg.split("-")
           verb=verb[-1]
           #print dep
           #print dep.values()[0][0]
 	   if dep.values()[0][0][0] not in listArg:
              listArg.append(dep.values()[0][0][0])
           if dep.values()[0][1][0] not in listArg:
              listArg.append(dep.values()[0][1][0])
        elif arg[0:4]=="Link":
           listLink.append(dep)
   #print listArg
   #print listLink
   for link in listLink:
       dep=link.keys()[0]
       vals=link[dep]
       val1=vals[0][0]
       val2=vals[1][0]
       #print val1, val2, verb
       if val1.split("-")[0]!=verb:
         if val1 in listArg:
             depFound=dep
             target=val1
             break
       elif val2.split("-")[0]!=verb :
          if val2 in listArg[0]:
             depFound=dep
             target=val2
             break


   if depFound!="":
      return depFound 



