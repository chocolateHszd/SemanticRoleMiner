#importing SenSta class for creating 
from StanSennaClass import SenSta
from FindPropArg import findArg
from FindPropArg import findPreds
from FindPropArg import mixDepArg
from FindPropArg import findDomain
from CreateRelations import makeRel
from CreateRelations import makeSt0
from CreateRelations import makeSt

#working with class object myTestFile
inputFile="~/srl/python/SemanticRoleMiner/testCases/test1/test_input.txt"
myTestFile=SenSta(inputFile)
myTestFile.makeSenna()
myTestFile.makeStanf()


#-- Test: PART1: getting info about sen0 from Senna and Stan ; generating labelels to each (Token,Token_Location)  
SEN0_SE=myTestFile.sennaDict['sen0']
SEN0_ST=myTestFile.stanfDict['sen0']
root=myTestFile.findRoot(SEN0_ST)
#print root
allPreds=findPreds(SEN0_SE)
#myTestFile.allPredicates=allPreds
#print allPreds

#---- testing predicates ------------
pred1=allPreds[1]
#print pred1
Col=pred1[1]
#print Col
root=pred1[0][0]
rootArgs= findArg(root,SEN0_SE,Col)
#print rootArgs

pred0=allPreds[0]
Col=pred0[1]
pred0=pred0[0][0]
pred0Args= findArg(pred0,SEN0_SE,Col)
#print pred0Args

#-------------------------------------
# Domain of each arg
rootArgsDomain=findDomain(rootArgs)
#print rootArgsDomain
pred0ArgDomain=findDomain(pred0Args)
#print pred0ArgDomain

#------------------------------------

#-- Test: PART2: combining dependecy-relations with labels ; A1=[ partmod[ (Token1,loc1),(Token2,loc2)] , ....      ]
rootMixedArgs=mixDepArg(SEN0_ST,rootArgs,root)
#print rootMixedArgs
pred0MixedArgs=mixDepArg(SEN0_ST,pred0Args,pred0)
#print pred0MixedArgs

#-----------------------------------
#-- Making relations
#print rootArgs

statement={}


rootSt0=makeSt0(root,rootArgs)
#print "St0-"+str(root)+": "+rootSt0
statement["St0-"+str(root)]=rootSt0
pred0St0=makeSt0(pred0,pred0Args)
#print "St0-"+str(pred0)+": "+pred0St0
statement["St0-"+str(pred0)]=pred0St0


#A2
i=0
rootSt1=makeSt("A2",root,rootMixedArgs,rootArgsDomain)
if rootSt1!=None:
   for item in rootSt1:
        #print "St0-"+str(root)+" "+item
	statement["St1"+str(i)+"-"+str(root)]="St0-"+str(root)+" "+item
        i+=1

i=0
pred0St1=makeSt("A2",pred0,pred0MixedArgs,pred0ArgDomain)
if pred0St1!=None:
   for item in pred0St1:
	#print "St0-"+str(pred0)+" "+item
	statement["St1"+str(i)+"-"+str(pred0)]="St0-"+str(pred0)+" "+item
        i+=1


#A3
rootSt2=makeSt("A3",root,rootMixedArgs,rootArgsDomain)
if rootSt2!=None:
   for item in rootSt2:
	#print "St0-"+str(root)+" "+item
	statement["St2"+str(i)+"-"+str(root)]="St0-"+str(root)+" "+item
        i+=1

pred0St2=makeSt("A3",pred0,pred0MixedArgs,pred0ArgDomain)
i=0
if pred0St2!=None:
   for item in pred0St2:
	#print "St0-"+str(pred0)+" "+item
	statement["St2"+str(i)+"-"+str(pred0)]="St0-"+str(pred0)+" "+item
        i+=1


#A4
rootSt3=makeSt("A4",root,rootMixedArgs,rootArgsDomain)
if rootSt3!=None:
   for item in rootSt3:
	#print "St0-"+str(root)+" "+item
	statement["St3"+str(i)+"-"+str(root)]="St0-"+str(root)+" "+item
        i+=1

pred0St3=makeSt("A4",pred0,pred0MixedArgs,pred0ArgDomain)
i=0
if pred0St3!=None:
   for item in pred0St3:
	#print "St0-"+str(pred0)+" "+item
	statement["St3"+str(i)+"-"+str(pred0)]="St0-"+str(pred0)+" "+item
        i+=1

#AM-TMP
i=0
rootSt4=makeSt("AM-TMP",root,rootMixedArgs,rootArgsDomain)
if rootSt4!=None:
   for item in rootSt4:
	#print "St0-"+str(root)+" "+item
	statement["St4"+str(i)+"-"+str(root)]="St0-"+str(root)+" "+item
        i+=1

i=0
pred0St4=makeSt("AM-TMP",pred0,pred0MixedArgs,pred0ArgDomain)
if pred0St4!=None:
   for item in pred0St4:
	#print "St0-"+str(pred0)+" "+item
	statement["St4"+str(i)+"-"+str(pred0)]="St0-"+str(pred0)+" "+item
        i+=1

#AM-DIS
rootSt5=makeSt("AM-DIS",root,rootMixedArgs,rootArgsDomain)
if rootSt5!=None:
   for item in rootSt5:
	#print "St0-"+str(root)+" "+item
	statement["St5"+str(i)+"-"+str(root)]="St0-"+str(root)+" "+item
        i+=1
pred0St5=makeSt("AM-DIS",pred0,pred0MixedArgs,pred0ArgDomain)
i=0
if pred0St5!=None:
   for item in pred0St5:
	#print "St0-"+str(pred0)+" "+item
	statement["St5"+str(i)+"-"+str(pred0)]="St0-"+str(pred0)+" "+item
        i+=1


print statement


