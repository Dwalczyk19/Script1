# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:58:39 2022

@author: Dave
"""

from matplotlib import pyplot as plt
import numpy as np 
import pandas as pandas
import time


#Frequency of each word and there usage 

class assessQuality(object): 
    def __init__(self,file): 
        self.L = []
        self.checkS = set()
        self.final = dict()
        self.countIstart = dict()
        self.countI = dict()
        self.responseLength = dict()
        self.wordLength = dict()
        self.totalOccurence = dict()
        self.insideFreq = dict() #Nested dictionary
        self.frequency = dict() #Final frequency dictionary
        

        
        oFile = open(file,"r",encoding="utf-8")
        for items in oFile: 
            items = items.strip()
            if items == "": 
                continue 
            else: 
                self.L.append(items)
               
                
    def parse(self): 
        #stop set
        for a in range(len(self.L)): 
            for b in range(len(self.L[a])): 
                if self.L[a][b].isalpha() or self.L[a][b].isnumeric() or self.L[a][b] == " " or self.L[a][b] == "." or self.L[a][b] == "$": 
                    continue
                else: 
                    self.checkS.add(self.L[a][b])
              
                    
        #final
        for c in range(len(self.L)): 
            temp = []
            for char in self.L[c]: 
                stringer = ""
                if char in self.checkS: 
                    continue
                else: 
                    temp.append(char)
            
            stringer = "".join(temp)
            self.final[c] = stringer
            
        
        #determine how many responses started with 
        for d,e in self.final.items(): 
            if e.startswith("I"): 
                self.countIstart[d] = True
            else: 
                self.countIstart[d] = False 
            
            
            if "I" in e: 
                iCount = e.count("I")
                self.countI[d] = iCount
                   
        
        #determine length of responses, count periods
        for f,g in self.final.items(): 
            countPeriod = 0
            countPeriod += g.count(".")
            countPeriod += g.count("?")
            countPeriod += g.count("!")
            self.responseLength[f] = countPeriod
            
        
        
        return (self.countIstart, self.countI, self.final, self.responseLength)


    def averageLength(self): 
        #average check set to remove all instances other than letters 
        tempDict = dict()
        averageS = set()
        for x in range(len(self.L)): 
            for y in range(len(self.L[x])): 
                if self.L[x][y].isalpha() or self.L[x][y] == " ": 
                    continue
                else: 
                    averageS.add(self.L[x][y])
                    
                    
        #bring together letters excluding all different types of char instances
        for i in range(len(self.L)):
            temp = []
            for char in self.L[i]: 
                stringer = ""
                if char in averageS: 
                    continue 
                else: 
                    temp.append(char)
                    
            stringer = "".join(temp)
            tempDict[i] = stringer
            
        
        #average length of words per response 
        for keys, values in tempDict.items(): 
            splitL = values.split()
            
            #seperate ct values to accurately determine each respective average length 
            per1 = 0
            per2 = 0
            ct2 = 0
            per3 = 0
            ct3 = 0
            per4 = 0
            ct4 = 0
            
            for items in splitL: 
                per1 += len(items)
                    
                if len(items) >= 4: 
                    ct2 += 1
                    per2 += len(items)
                    
                if len(items) >= 5: 
                    ct3 += 1
                    per3 += len(items)
                    
                if len(items) >= 6: 
                    ct4 += 1
                    per4 += len(items)
                    
            
            avg1 = round((per1/len(splitL)),4) #every word
            avg2 = round((per2/ct2),4) #len of words 4 and above
            avg3 = round((per3/ct3),4) #len of words 5 and above 
            avg4 = round((per4/ct4),4) #len of words 6 and above
            self.wordLength[keys] = [avg1,avg2,avg3,avg4]
            
        
        
        return self.wordLength
               
    def occurence(self): 
        
        
        #SIMPLE PARSE OF FINAL DICTIONARY
        #Ill make an alias to avoid any overlapping of dictionaries
        
        fin = []
        for i in range(len(self.L)): 
            words = self.L[i].split()
            for items in words: 
                temp = []
                for char in items:
                    string = ""
                    if not char.isalpha(): 
                        continue 
                    else: 
                        temp.append(char)
                
                string = "".join(temp)
                if string == "" or len(string) == 1: 
                    continue
                else:
                    fin.append(string)
                
        
        for items in fin: 
            items = items.lower()
            count = fin.count(items)
            self.totalOccurence[items] = count

        return self.totalOccurence

if __name__ == "__main__": 
    

    Q1 = assessQuality("Q1Answers.txt")
    Q1countIStart, Q1count, Q1dict, Q1rLength = Q1.parse()
    Q1average = Q1.averageLength() 
    
    Q2 = assessQuality("Q2Answers.txt")
    Q2countIstart, Q2count, Q2dict, Q2rLength = Q2.parse()
    Q2average = Q2.averageLength()
    
    Q3 = assessQuality("Q3Answers.txt")
    Q3countIstart, Q3count, Q3dict, Q3rLength = Q3.parse()
    Q3average = Q3.averageLength()
    
    Q4 = assessQuality("Q4Answers.txt")
    Q4countIstart, Q4count, Q4dict, Q4rLength = Q4.parse()
    Q4average = Q4.averageLength()
    
    Q5 = assessQuality("Q5Answers.txt")
    Q5countIstart, Q5count, Q5dict, Q5rLength = Q5.parse()
    Q5average = Q5.averageLength()
    
    #print(Q1countIStart,"\n")
    #print(Q1average,"\n\n",Q2average,"\n\n",Q3average,"\n\n",Q4average,"\n\n",Q5average,sep="")
    

