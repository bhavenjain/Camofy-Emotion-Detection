from statistics import mode
import gad
import statistics
import time
import os
import platform

def clrscr():
    os.system('cls' if platform.system().lower().startswith("win") else 'clear')

def MostCommon(list):
    return(mode(list))

gad.main()
clrscr()
print(MostCommon(gad.AgeList))
print(MostCommon(gad.GenderList))
