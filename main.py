#importing SenSta class for creating 
from StanSennaClass import SenSta
from FindPropArg import findArg

#working with class object myTestFile
inputFile="~/srl/python/SemanticRoleMiner/test/test_input1.txt"
myTestFile=SenSta(inputFile)
myTestFile.makeSenna()
myTestFile.makeStanf()

var1=myTestFile.sennaDict['sen0']
var2=myTestFile.stanfDict['sen0']['root']
findArg(var2,var1)
