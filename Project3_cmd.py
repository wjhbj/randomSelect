#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

import random
import linecache
def Button_2_onCommand(uiName,widgetName):
    openPath=tkinter.filedialog.askopenfilename(initialdir=os.path.abspath('.'),title='Open File',filetypes=[('Python File','*.txt'),('All files','*')])
    if openPath != None:
        Fun.SetText(uiName,'Label_4',openPath)
        count = len(open(openPath,'rU',encoding="utf-8").readlines())

        hellonum=random.randrange(1,count+1, 1)
        Fun.SetText(uiName,'Label_7','随机选择结果:'+linecache.getline(openPath,hellonum))
def Button_8_onCommand(uiName,widgetName):
        textAddress=Fun.GetText(uiName,'Label_4')
        count = len(open(textAddress,'rU',encoding="utf-8").readlines())#获取行数
        hellonum=random.randrange(1,count+1, 1)#生成随机行数
        Fun.SetText(uiName,'Label_7','随机选择结果:'+linecache.getline(textAddress,hellonum))#随机读取某行

