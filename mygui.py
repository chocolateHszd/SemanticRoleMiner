import wx
class ViewResults(wx.Frame):
   def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame SemSen',size=(800,500))
        
        #homeBox=wx.BoxSizer(wx.VERTICAL)
        panel=wx.Panel(self)
        
        
        #--- text experiments
        #-- static text
        userInput=wx.StaticText(panel,-1,"Type here...",(10,10),(260,-1))#,wx.ALIGN_CENTER)
        	#tweaking the color
        	#userInput.setForegroundColour('white')
       		#userInput.setBBackgroundColour('blue')
        
        text1=wx.TextEntryDialog(None,"name?","title","name here")
        if text1.ShowModal()==wx.ID_OK:
           answer=text1.GetValue()
        wx.StaticText(panel,-1,answer,(20,20))

        
        #--- creating Box and binding functions to it
        startbutton=wx.Button(panel,label="Start",pos=(30,100),size=(50,30))
        #self.Bind(wx.EVT_BUTTON,self.closeButton,closebutton)
        self.Bind(wx.EVT_CLOSE,self.closeWindow)
        




        #---- creating a messageBox
	#box=wx.MessageDialog(None,'Hi','Title',wx.YES_NO)   # wx.OK, 
        #answer=box.ShowModal() # the values of box that user selected
        #box.Destroy()
   
        #---- creating TextBox , input user
        #txtBox=wx.TextEntryDialog(None,"Hi","Title","default text")
        #if txtBox.ShowModal()==wx.ID_OK:
        #   answer=txtBox.GetValue()
        
        #-- organizing panels        
        #homeBox.Add(inputPanel,1,wx.EXPAND | wx.ALL,3)
        #homeBox.Add(resultPanel,1,wx.EXPAND | wx.ALL,3)



   #def closeButton(self,event):
   #    self.Close(True)
   def closeWindow(self,event):
       self.Destroy()