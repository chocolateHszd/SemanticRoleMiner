#importing SenSta class for creating 
from StanSennaClass import SenSta
from FindPropArg import findArg
from FindPropArg import findPreds
from FindPropArg import mixDepArg
from FindPropArg import findDomain
from CreateRelations import makeRel
from CreateRelations import makeSt0
from CreateRelations import makeSt
from CreateRelations import makeSubSt
from CreateRelations import verbDepArg



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
rootArgDomain=findDomain(rootArgs)
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

args={"A2":"St1","A3":"St2","A4":"St3","AM-TMP":"St4","AM-DIS":"St5"}
statement={}


rootSt0=makeSt0(root,rootArgs)
#print "St0-"+str(root)+": "+rootSt0
statement["St0-"+str(root)]=rootSt0
pred0St0=makeSt0(pred0,pred0Args)
#print "St0-"+str(pred0)+": "+pred0St0
statement["St0-"+str(pred0)]=pred0St0

predicates=[]
for key,val in allPreds.items():
    predicates.append(val[0][0])
#print pr

for arg,st in args.items():
   i=0
   #print root
   rootSt=makeSt(arg,root,rootMixedArgs,rootArgDomain)
   if rootSt!=None:
      for item in rootSt:
         #print "St0-"+str(root)+" "+item
	 statement[str(st)+str(i)+"-"+str(root)]="St0-"+str(root)+" "+item
         i+=1
   i=0
   pred0St=makeSt(arg,pred0,pred0MixedArgs,pred0ArgDomain)
   if pred0St!=None:
      for item in pred0St:
	 #print "St0-"+str(pred0)+" "+item
	 statement[str(st)+str(i)+"-"+str(pred0)]="St0-"+str(pred0)+" "+item
         i+=1

#print statement


#-----------------------------------
#--verbDependencyArg
start=100
vda=verbDepArg(root,rootMixedArgs,rootArgDomain)
for tuples in vda.values():
    statement[str(start)]=tuples[0]+" "+tuples[1]+" "+tuples[2]
    start+=1

vda=verbDepArg(pred0,pred0MixedArgs,pred0ArgDomain)
for tuples in vda.values():
    statement[str(start)]=tuples[0]+" "+tuples[1]+" "+tuples[2]
    start+=1

#-----------------------------------
#-- makeSubRelations

values=statement.values()
newSts=makeSubSt(root,rootMixedArgs)
for item in newSts.values():
    thing=item[0]+" "+item[1]+" "+item[2] 
    if thing not in values and (item[0] not in predicates) and (item[2] not in predicates):
      # print thing
       statement[str(start)]=item[0]+" "+item[1]+" "+item[2]
       start+=1


values=statement.values()
newSts=makeSubSt(pred0,pred0MixedArgs)
for item in newSts.values():
    #print item
    thing=item[0]+" "+item[1]+" "+item[2]
    
    if thing not in values and (item[0] not in predicates) and (item[2] not in predicates):
      # print thing
       statement[str(start)]=item[0]+" "+item[1]+" "+item[2]
       start+=1

print statement



