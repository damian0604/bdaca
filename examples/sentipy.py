#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import subprocess
import os
import csv

dir=os.path.dirname(os.path.abspath(__file__))

def senti(doc,lang):
    ''' 
    Takes a string with text as well as the language (e.g., dutch) as input
    returns a (negative,positive) tuple
    '''

    command = "echo {0} | java -jar {1}/SentiStrengthCom.jar stdin sentidata {1}/{2}/ utf8".format(doc.replace("\n"," ").replace("\r"," ").replace('"'," ").replace("'"," ").replace("("," ").replace(")"," ").replace("|"," ").replace("<"," ").replace(">"," ").replace(";",",").replace("&"," ").replace("#"," ").replace("`"," ").replace("´"," "),dir,lang.lower())
    response = subprocess.check_output(command, shell=True).decode("utf-8").strip().split("\t")
    return(tuple(int(el) for el in response))

def sentifile(filename,lang,includetext=False):
    ''' 
    Takes a filename with one text per lineas well as the language (e.g., dutch) as input
    returns a list of (negative,positive) tuples
    If includetext=True, the tuple is: (negative,positive,text) 
    '''

    command = "java -jar {1}/SentiStrengthCom.jar input {0} resultsExtension .out sentidata {1}/{2}/ utf8".format(filename,dir,lang.lower())
    responsexxx = subprocess.check_output(command, shell=True).decode("utf-8").strip().split("\t")
    #print(command)    
    #print(responsexxx)    
    outputfilename=os.path.splitext(filename)[0]+"0.out"
    response=[]    
    with open(outputfilename, mode="r", newline="") as fi:
        reader=csv.reader(fi,delimiter="\t")
        next(reader)
        if includetext:
            for row in reader:
                response.append(tuple([row[0],row[1],row[2]]))           
        else:
            for row in reader:
                response.append(tuple([row[0],row[1]]))
    os.remove(outputfilename)
    return(response)



if __name__ == "__main__":
    sentence="Ik hou van honden, maar aan katten heb \nik echt een hekel."
    language="dutch"
    resp=senti(sentence,language)
    print("Evaluating a",language,"sentence: ",sentence)
    print("Negativity",resp[0])
    print("Positivity",resp[1])

