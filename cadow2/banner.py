import os
import time

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

green = '\033[32;1m'

gta = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

white = '\033[1;37m' # White 
red = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan
green = ("\033[92m")
pryellow = ("\033[93m")
prLightPurple=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")


class banner:
    def __init__(self):
        print pryellow+"""
                       _         _
__      _____  _ __ __| | (_)___| |_
\ \ /\ / / _ \| '__/ _` | | / __| __|
 \ V  V / (_) | | | (_| | | \__ \ |_
  \_/\_/ \___/|_|  \__,_|_|_|___/\__|
          [Wordlist Generator new 2019]
        [@Created By Cabdualahi Sharif] """+C+p+"""
       Youtube Channel: Somali 4You
       facebook : cabdulahi.sharif.100
       github: https://github.com/Cabdulahi
       dev: Cabdulahi Sharif Gsm
       program type: Python
       
       """
        print (red+'-')*43
        
        
        
       