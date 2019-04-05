#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import pandas as pd
from datetime import datetime
from pandas.io import sql
import pickle

#advance current month by one. increases year if dec
def addMonth(month,year):
    if month == '12':
        return '01',str(int(year)+1)
    elif int(month) < 9:
        return '0'+str(int(month)+1),year
    else:
        return str(int(month)+1),year

def processOneTable(table,states,newEntries,missed,idNum):
    for index, row in table.iterrows():
        try:
            if states[row['State']][row['City']] != None:
                newEntries.append([row['Date / Time'],states[row['State']][row['City']],row['Shape'],row['Summary'],duration(row['Duration'])])
                idNum+=1
        except KeyError:
            missed.append([row['Date / Time'],row['State'],row['City'],row['Shape'],row['Summary'],duration(row['Duration'])])

def duration(duration):
    number = 0
    foundNum = False
    time = ''
    decimal = False
    decimalCount = 0
    timeFormat = False

    duration = str(duration)

    for letter in duration:
        if letter == '.':
            decimal = True
        elif letter == ':':
            timeFormat = True
        else:
            try:
                num = int(letter)
                if decimal:
                    decimalCount+=1
                    number = number*10 + num
                #approximates the time in seconds (does not count the x in 00:0x)
                elif timeFormat:
                    return number*360+num*60
                else:
                    number = number*10 + num
                    foundNum = True

            except:
                #print('on except')
                if decimal:
                    number = number/(10**decimalCount)
                    decimal = False
                if letter != ' ' or letter != '~' or letter != '<' or letter != '>':
                    time+=letter
                if foundNum:
                    if time == 'sec':
                        return number
                    elif time == 'min':
                        return number*60
                    elif time == 'hr' or time == 'hour':
                        return number*360
    return 'NaN'

pdTables = []

lastMonth = '201505'
idNum = 10000 #some db shit...: "select max(id) from UFO_table"+1
missedWebsite = []
count = 0
stopMonth = '201809'
currentMonth = int(datetime.today().strftime("%Y%m"))

def getWebsiteInfo()
    count = 0
    while year+month != currentMonth and count <= limit:
        try:
            print('getting data from: '+ 'http://www.nuforc.org/webreports/ndxe'+year+month+'.html')
            #newTable = pd.read_html('http://www.nuforc.org/webreports/ndxe'+year+month+'.html')
            monthsObtained.append(year+month)
        except:
            missedWebsite.append(year+month)

        month,year = addMonth(month,year)
        #pdTables.append(newTable[0])
        processOneTable(newTable[0],states,newEntries,missedEntries,idNum)
        count = 1

        return pdTables

def makeCityFinder():
    states = {}

    with open ('2010.csv') as censusZip:
        censusInfo = csv.reader(censusZip,delimiter=',')
        header = True
        for row in censusInfo:
            if header:
                header = False
            else:
                if states.get(row[8]) == None:
                    states[row[8]] = {}
                    states[row[8]][row[7]] = (row[9],row[10])
                else:
                    states[row[8]][row[7]] = (row[9],row[10])
    return states
