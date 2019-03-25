#!/usr/bin/python
# coding=utf-8
#//Coded By Cabdulahi Sharif 
'''Read My Script Up . I don't like to encrypt my source .broo enjoy it 
'''

import time,os
import struct
import sys
import itertools
import banner
prred = ("\033[91m")
green = ("\033[92m")
pryellow = ("\033[93m")
prLightPurple=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")
p  = '\033[35m' # purple
c  = '\033[36m' # cyan



class you:
    def __init__(self):
        print
        self.ohh= time
       
        self.boss = (pryellow+'Cabdulahi=>>: ')
        print
        print (pryellow+' [💾]Find The File /sdcard/wordlists.txt')
        print
        print
        self.cu = str(raw_input(pryellow+'[📝]Insert Custom word: '))
        self.ohh.sleep(1)
        
        print
        self.min = int(raw_input(pryellow+'[📝]Min Length: '))
        self.ohh.sleep(1)
        print
        self.max = int(raw_input(pryellow+'[📝]Max Length: '))
        self.ohh.sleep(1)
        return self.cabdualhi()
    def mom(self):
        
        print
        
        self.get = raw_input(self.boss)
        print
        if (self.get=='1' or self.get=='one'):
            return self.lowercase()
        elif(self.get=='2' or self.get=='two'):
            return self.uppercase()
        elif(self.get=='3' or self.get=='three'):
            return self.num()
        elif(self.get=='4' or self.get=='four'):
            return self.sp()
        else:
            return self.mom()
    def cabdualhi(self):
        print
        print (c+p+'       [📌]Choose Any Character ')
        print
        print prred+' [{1}]'+pryellow+'Lower-Case[a-z]'
        print prred+' [{2}]'+pryellow+'Upper-Case[A-Z]'
        print prred+' [{3}]'+pryellow+'Numbers[0-9]'
        print prred+' [{4}]'+pryellow+'Special Characters[@#?$%(And More )]'
        return self.mom()
    def num(self):
        print
        self.ohh.sleep(1)
        lat = ('0123456789')
        war= itertools.permutations(lat,self.max)
        fil = open('/sdcard/wordlists.txt','w')
        for x in war:
            self.creat= '\n'+self.cu+('').join(x)
            for g in self.creat:
                fil.write(g)
    def lowercase(self):
        print
        alp = ('abcdefghijklmnopqrstuvwxyz')
        war= itertools.permutations(alp,self.max)
        fil = open('/sdcard/wordlists.txt','w')
        for x in war:
            self.creat= '\n'+self.cu+('').join(x)
            
            for g in self.creat:
                fil.write(g)           
    def k(self):
        self.ohh.sleep(1)
        print
        print (pryellow+'[✏]Creating Wordlist Texts')
        print (pryellow+'[✔]Successful Created') 
    def uppercase(self):
        al = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        warr= itertools.permutations(al,self.max)
        fil = open('/sdcard/wordlists.txt','w')
        for x in warr:
            self.creat= '\n'+self.cu+('').join(x)
            for g in self.creat:
                fil.write(g)    
    def sp(self):
        all = ('''@#$%&-+()*"':;!?,_/.~`|•√π÷×¶∆£¢€¥^°={}\©®™℅[],<>.''')
        wa= itertools.permutations(all,self.max)
        fil = open('/sdcard/wordlists.txt','w')
        for x in wa:
            self.creat= '\n'+self.cu+('').join(x)
            for g in self.creat:
                fil.write(g)