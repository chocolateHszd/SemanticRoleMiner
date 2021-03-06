#for using terminal , calling senna and stanford parser
import os
from sennaProcessed import modifySenna
from stanfProcessed import modifyStanf

class SenSta:

   inputFile="Null"
   sennaOutFile=""
   stanOutFile =""
   sennaDict={}
   stanfDict={}
   root=""
   rootArgsDomain={}
   allPredicates={}
   def __init__(self,arg):
	self.inputFile="/home/kimia/"+arg+"/test_input.txt"
        #print "*&*&*"+arg + "&^&^&^"+ self.inputFile
        self.sennaOutFile="/home/kimia/"+arg+"/senna"
        self.stanOutFile="/home/kimia/"+arg+"/stan"

   def makeSenna(self):
        #running senna to generate sennaoutput 
        cmd=os.system('cd /home/kimia/srl/senna \n ./senna <'+self.inputFile+'> '+self.sennaOutFile+'output.txt')
        self.sennaDict=modifySenna(self.sennaOutFile+'output.txt')
        return self.sennaDict 
                  

   def makeStanf(self):
        cmd=os.system('cd /home/kimia/srl/stanford-parser/ \n ./lexparser.sh '+self.inputFile+' >'+self.stanOutFile+'output.txt')
        self.stanfDict=modifyStanf(self.stanOutFile+'output.txt')
        return self.stanfDict

   def findRoot(self,Sen):
        dep=""
        for val in Sen.values():
            dep=val.keys()
	    vals=val.values()
            vals=vals[0]
            dep=dep[0]
            if dep=="root":
               return vals[1] 




