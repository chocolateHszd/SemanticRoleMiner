
def verbDepArg(verb,Args,Domains,Predicates):
   #print Args
   results={}
   tokens=Args.values()
   dom1=Domains.values()
   #print Domains
   counter=0
   for key in tokens:
       label=key.keys()[0]
       dep=key.values()[0].keys()[0]
       token=key.values()[0].values()[0]
       token1=token[0][0]
       token2=token[1][0]
       if label==( "Link-"+str(verb.split("-")[0])):
          #print "label"
          #print label,token1,token2
          val=int(token1.split("-")[-1])
          tok=token1
          lab=""
          if token1==verb:
              val=int(token2.split("-")[-1])
              tok=token2
          for a,dom in Domains.items():
              domain=dom
              d1=domain[0]
              d2=domain[1]
              if val>=int(d1) and val<=int(d2):
                 lab=a
                 #print "*"
                 #print lab, tok, val, d1,d2
                 #print "----"
          #print lab,tok,dep
          if tok in Predicates:
	     #print tok
             tok="St0-"+str(tok)
          results[counter]=(lab+"-"+str(verb.split("-")[-1]),dep,tok)
          counter+=1
   return results



def subSt(verb,Args,Predicates,statements):
   newSts={}
   counter=0
   sw=0
   values=statements.values()
   tokens=Args.values()
   for item in tokens:
       if item.keys()[0]!= "Link-"+str(verb.split("-")[0]):
               #print item.keys()[0]
	       fruit=item.values()[0]
	       dep=fruit.keys()[0]
	       token1=fruit.values()[0][0][0]
	       token2=fruit.values()[0][1][0]
	       #print dep,token1,token2 
               toAdd=token2+" "+dep+" "+token1
               #print len(toAdd), toAdd
               if token2 in Predicates :
                  sw=0
                  for i in values:
                     #print i,"----"+ i[len(i)-len(toAdd):]
                     exception=i[len(i)-len(toAdd):]
                     if toAdd==exception:
                        sw=1
                  if sw==0:
 		     token2="St0-"+str(token2)
               newSts[counter]=(token1,dep,token2)
               counter+=1
   return newSts

#------------------------------------------------
def makeStatements(PRED,ARGDOM,MIXARGS):
    statement={}
    start=100
    for key,verb in PRED.items():
	vda=verbDepArg(verb,MIXARGS[key],ARGDOM[key],PRED.values())
	fixSt0="St0-"+verb
	#print vda
	for tuples in vda.values():
	    test=fixSt0+" "+tuples[0].split("-")[0]+" "+tuples[0]
	    #print test
	    if test not in statement.values():
	       statement[str(start)]=test
	       start+=1
	    statement[str(start)]=tuples[0]+" "+tuples[1]+" "+tuples[2]
	    start+=1

	#-----------------------------------
	#-- makeSubRelations ---- ^-^---- it finds tokens and inter-dependencies among them 

    for key,verb in PRED.items():
	values=statement.values()
	newSts=subSt(verb,MIXARGS[key],PRED.values(),statement)
	for item in newSts.values():
	    thing=item[0]+" "+item[1]+" "+item[2] 
	    thing2=item[2]+" "+item[1]+" "+item[0]
	    if (thing not in values) and (thing2 not in values) and (item[0] not in PRED.values()) and (item[2] not in PRED.values()):
		  # print thing
		  statement[str(start)]=item[0]+" "+item[1]+" "+item[2]
		  start+=1

    return statement



