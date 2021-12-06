#coding=utf-8
#import libs 
import sys
import Project3_cmd
import Project3_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Project3:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = Project3_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,640,480)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 640,height = 480)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Button_2 = tkinter.Button(Form_1,text="请选择文件",width = 10,height = 4)
        Fun.Register(uiName,'Button_2',Button_2)
        Button_2.place(x = 100,y = 150,width = 100,height = 28)
        Button_2.configure(command=lambda:Project3_cmd.Button_2_onCommand(uiName,"Button_2"))
        Label_4 = tkinter.Label(Form_1,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_4',Label_4)
        Label_4.place(x = 100,y = 200,width = 450,height = 50)
        Label_4.configure(relief = "flat")
        Label_7 = tkinter.Label(Form_1,text="Label",width = 10,height = 4)
        Fun.Register(uiName,'Label_7',Label_7)
        Label_7.place(x = 100,y = 300,width = 450,height = 50)
        Label_7.configure(relief = "flat")
        Button_8 = tkinter.Button(Form_1,text="重新选择",width = 10,height = 4)
        Fun.Register(uiName,'Button_8',Button_8)
        Button_8.place(x = 111,y = 376,width = 100,height = 28)
        Button_8.configure(command=lambda:Project3_cmd.Button_8_onCommand(uiName,"Button_8"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = Project3(root)
    root.mainloop()
