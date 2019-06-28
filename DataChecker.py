# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# working on anaconda python distribution with pandas 0.24

df = pd.read_csv("27018_gdf.csv")
df[["day","month","year"]] = df.data.str.split(".", expand=True,)
dictDates = ["31","28","31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]


def leapYear(y):
    return (y %  4 ==0 ) and (y  % 100 != 0 ) or (y % 400 == 0)

def checkDuplicateDates():
    duplicate = df[df.columns[0]].dropna().duplicated()
    a = np.where(duplicate == True)
    return len(a[0]) 

def checkDuplicateValues():
    duplicate = df[df.columns[1]].dropna().duplicated()
    a = np.where(duplicate == True)
    return len(a[0])

def parseMonth():
    counterMerr = 0
    counterRowM = 1
    j = 1
    for m in df['month']:
        if counterRowM > int(dictDates[j-1]):
            j +=1 
            counterRowM = 1 
        if m == str(j).zfill(2) and m !=None:
            counterRowM += 1 
        elif m == None:
            counterRowM += 1
            counterMerr += 1 
    return counterMerr

#count missing days in date
def parseDay():
    j = 0
    counterRowD = 1
    counterNaND = 0 #count missing date
    for d in df['day']:
        if counterRowD > int(dictDates[j-1]):
            j +=1
            counterRowD = 1
        if type(d)==float:
            counterRowD += 1
            counterNaND += 1
            continue
        counterRowD += 1
    return counterNaND

def checkLeapYear():
    countLeap = 0
    countNotLeap = 0
    counterYerr = 0
    for y in df['year']:
        if y == None:
            counterYerr += 1 
        elif leapYear(int(y)):
            countLeap += 1
        else:
            countNotLeap += 1
    if countLeap > countNotLeap:
        return "year in dataset is leap year"
    else:
        return "year in dataset is not leap year"
        
def checkYear():
    counterRowY = 1
    counterYerr = 0
    for y in df['year']:
        if y == None:
            counterYerr += 1
    return counterYerr

def checkValues():
    counterVerr = 0
    values = df[df.columns[1]]
    for v in values:
        if str(v) == "nan":
            counterVerr +=1
    return counterVerr
def generateReport():
    mM = parseDay()
    mD = parseMonth()
    ly = checkYear()
    v = checkValues()
    dupli = checkDuplicateDates()
    values = checkDuplicateValues()
    lp = checkLeapYear()
    
    print(df)
    print(str(lp))
    print("Missing Days in date: " + str(mD))
    print("Missing Months in date: " + str(mM))
    print("Missing Years in date: " + str(ly))
    print("Missing values in dataset: " + str(v))
    print("Duplicates in date: " + str(dupli))
    print("Duplicates in values: " + str(values))
    
generateReport()






