#importing SenSta class for creating 
from StanSennaClass import SenSta
from FindPropArg import findArg
from FindPropArg import findPreds
from FindPropArg import mixDepArg
from FindPropArg import findDomain
from CreateRelations import makeStatements
from CreateRelations import subSt
from CreateRelations import verbDepArg
from Visualizer import makeGephi


#working with class object myTestFile
inputFile="srl/python/SemanticRoleMiner/testCases/test1"
myTestFile=SenSta(inputFile)
myTestFile.makeSenna()
myTestFile.makeStanf()


SEN0_SE=myTestFile.sennaDict['sen0']
SEN0_ST=myTestFile.stanfDict['sen0']
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


#-------------------------------------
# Domain of each arg
ARGDOM={} #
MIXARGS={}
for key,val in ARGS.items():
    ARGDOM[key]=findDomain(val)
    MIXARGS[key]=mixDepArg(SEN0_ST,ARGS[key],PRED[key])


#-----------------------------------

statement={}
start=100

#-----------------------------------
# manipulating all statements 

statement=makeStatements(PRED,ARGDOM,MIXARGS)
print statement

#---------------------------------------------
#-- visualization

#makeGephi(statement,inputFile)



