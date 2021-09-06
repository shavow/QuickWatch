#███████╗██╗  ██╗ █████╗ ██╗   ██╗ ██████╗ ██╗    ██╗
#██╔════╝██║  ██║██╔══██╗██║   ██║██╔═══██╗██║    ██║
#███████╗███████║███████║██║   ██║██║   ██║██║ █╗ ██║
#╚════██║██╔══██║██╔══██║╚██╗ ██╔╝██║   ██║██║███╗██║
#███████║██║  ██║██║  ██║ ╚████╔╝ ╚██████╔╝╚███╔███╔╝
#╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚══╝╚══╝ 

import sys, threading, subprocess, psutil, shutil, pathlib, multiprocessing, PIL, os
import random, math, time, datetime
import pydirectinput, pynput, pyautogui
from datetime import datetime
from shutil import copy, copyfile, copy2
from pynput import keyboard 
from os.path import abspath, isfile, isdir
from os import path, mkdir, read, rename, times, listdir, scandir, close, name
from threading import Thread
from PIL import ImageColor, ImageTk
from multiprocessing import Process
from math import *

#]____________________[ global-variables ]____________________[#

_userPath =os.path.expanduser("~") +"\\"
_userName =_userPath.split("\\")[-2]
_appDataPath =_userPath +"AppData\\"

_roamingPath =_appDataPath +"Roaming\\"
_folderPath =_roamingPath +"QuickWatch\\"
_autosavingFolder =_folderPath +"Auto-Saving\\"

_filePath =_folderPath +f"{_userName}.sys"

#]____________________[ installer-here ]____________________[#

def recovery():
    if os.path.isfile(_filePath):
        pass
    else:
        scanned =0
        listedFiles =[]
        for file in os.scandir(_autosavingFolder):
            if os.path.isfile(os.path.abspath(file)):
                scanned +=1
                listedFiles.append(os.path.abspath(file))
        if scanned == 0:
            open(_filePath, "w+").write(f"counts._0|")
        elif scanned >0:
            shutil.copyfile(listedFiles[-1], _filePath)


def downloadFolders():
    if os.path.isdir(_roamingPath):

        if os.path.isdir(_folderPath): #main folder directory
            pass
        else:
            os.mkdir(_folderPath)
        
        if os.path.isdir(_autosavingFolder): #auto-saving folder 
            pass
        else:
            os.mkdir(_autosavingFolder)

        if os.path.isfile(_filePath): #file recorder
            pass
        else:
            recovery()

downloadFolders()

#]____________________[ commands-here ]____________________[#

def ongoingTimer(): #timer control
    while True:
        time.sleep(1) #waits one second
        if os.path.isfile(_filePath):
            file =open(_filePath, "r+").read()

            #get-number --
            stringNumber =file[file.find("_")+1:file.find("|")]
            if stringNumber.isdigit():
                a =int(stringNumber)
                a +=1
                b =str(a)
                file =open(_filePath, "w+").write(f"counts._{b}|")
        else:
            recovery()

def autosavingFiles(): #auto-saving files
    while True:
        if os.path.isfile(_filePath):
            shutil.copyfile(_filePath, _autosavingFolder +str(datetime.now()).replace(":",".") +".txt")
        time.sleep(240) #4 minutes

def deleteAutosaves():
    while True:
        time.sleep(120) #checks for auto-saves every 2 minutes
        scannedList =[]
        scanned =0
        for file in os.scandir(_autosavingFolder):
            if os.path.isfile(os.path.abspath(file)):
                scannedList.append(os.path.abspath(file))
                scanned +=1
        if scanned >19: #if there is 20 files
            for x in range(14):
                os.remove(scannedList[x]) #delete 15 oldest files

#]____________________[ threading-here ]____________________[#
    
Thread(target=ongoingTimer).start()
Thread(target=autosavingFiles).start()
Thread(target=deleteAutosaves).start()