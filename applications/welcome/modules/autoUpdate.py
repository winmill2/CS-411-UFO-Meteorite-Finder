# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime
#from pandas.io import sql
import pickle
import csv
import sys
#from gluon import current
#import db as database

#formats time into appropriate format
def formatDateTime(time):
    try:
        timeFormat = datetime.strptime(time,'%m/%d/%y %H:%M')
        return timeFormat.strftime('%Y-%m-%d %H:%M:%S')
    except:
        timeFormat = datetime.strptime(time,'%m/%d/%y')
        return timeFormat.strftime('%Y-%m-%d %H:%M:%S')

#advance current month by one. increases year if dec
def addMonth(year,month):
    if month == '12':
        return str(int(year)+1),'01'
    elif int(month) < 9:
        return year,'0'+str(int(month)+1),
    else:
        return year, str(int(month)+1),

#adds records from one month's table
def processOneTable(table,states,db):
    error = " no errors on adding table "
    print("in process One table. check state:",states['MT']['Butte'])
    for index, row in table.iterrows():
        try:
            if states[row['State']][row['City']] != None:
                newGeoLoc = states[row['State']][row['City']]
                strLoc = '('+newGeoLoc[0]+','+newGeoLoc[1]+')'
                #print("adding:",row['State'],row['City'],states[row['State']][row['City']])
                newUFOId = db.UFO_table.insert(datetime= formatDateTime(row['Date / Time']),GeoLocation= strLoc, shape= row['Shape'], comments=row['Summary'] ,duration_sec=duration(row['Duration']))
                newLocId = db.Location_table.update_or_insert(GeoLocation= strLoc, latitude=newGeoLoc[0], longitude=newGeoLoc[1], city=row['City'], state=row['State'], country= 'us')

        except KeyError:
            print(row['State'],row['City']," not there")
        except Exception:
            print(sys.exc_info())
    return error

#converts duration to seconds
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
                    foundNum = True
                #approximates the time in seconds (does not count the x in 00:0x)
                elif timeFormat:
                    return number*60+num*10
                else:
                    number = number*10 + num
                    foundNum = True

            except:
                #print('on except')
                if decimal:
                    number = number/(10**decimalCount)
                    decimal = False
                if letter != ' ' and letter != '~' and letter != '<' and letter != '>':
                    time+=letter
                if foundNum:
                    #print("Found Num",time)
                    if time == 'sec':
                        return number
                    elif time == 'min':
                        return number*60
                    elif time == 'hr' or time == 'hour':
                        return number*360
    return 0

def getUploaded():
    try:
        uploaded = pickle.load(open('uploaded.p','rb'))
    except:
        uploaded = []
    return uploaded

def getMissed():
    try:
        missed = pickle.load(open('missed.p','rb'))
    except:
        missed = []
    return missed

def getPdTable():
    try:
        pdTable = pickle.load(open('pdTable.p','rb'))
    except:
        pdTable = []
    return pdTable

#returns: year,month as strings
def startMonth(upLoadedMonths):
    length = len(upLoadedMonths)
    #print upLoadedMonths
    if length == 0:
        return '2015','07' #when our info ends (technically 5/8/15)
    else:
        #call addmonth,year,month
        return addMonth(upLoadedMonths[length-1][0],upLoadedMonths[length-1][1])
        #return upLoadedMonths[length-1][0],upLoadedMonths[length-1][1]

def runUpdate(db):
    missedMonths = getMissed()
    upLoadedMonths = getUploaded()
    states = makeCityFinder()
    year,month = startMonth(upLoadedMonths)
    pdTables = getPdTable()

    #db = current.db#globalenv['db']

    message = getWebsiteInfo(year,month,upLoadedMonths,missedMonths,pdTables,states,db)
    #message = processOneTable(pdTables[0],states,db)

    pickle.dump(pdTables,open('pdTable.p','wb'))
    pickle.dump(upLoadedMonths, open('uploaded.p','wb'))
    pickle.dump(missedMonths, open('missed.p','wb'))

    return upLoadedMonths
    #return "this was last month added " + year + month + '\n' + str(message)

def getWebsiteInfo(year,month,uploadedMonths,missedMonths,pdTables,states,db):
    count = 0
    currentMonth = datetime.today().strftime("%Y%m")
    limit = 1
    message = "did not get website data"
    while year+month != currentMonth and count < limit:

        print("going for "+'http://www.nuforc.org/webreports/ndxe'+year+month+'.html')
        newTable = pd.read_html('http://www.nuforc.org/webreports/ndxe'+year+month+'.html')
        uploadedMonths.append((year,month))
        #print('http://www.nuforc.org/webreports/ndxe'+year+month+'.html')
        month,year = addMonth(year,month)
        pdTables.append(newTable[0])
        message = processOneTable(newTable[0],states,db)
        count+= 1

    return message

def makeCityFinder():
    try:
        states = pickle.load(open('states.p','rb'))
    except:
        states = {}
        with open ('cityStates.csv') as censusZip:
            censusInfo = csv.reader(censusZip,delimiter=',')
            for row in censusInfo:
                if states.get(row[0]) == None:
                    states[row[0]] = {}
                    states[row[0]][row[1]] = (row[2],row[3])
                else:
                    states[row[0]][row[1]] = (row[2],row[3])
        pickle.dump(states, open('states.p','wb'))
    return states

#def main():
    #database = current.globalenv['db']
    #  message = runUpdate()
    # return message

#if __name__ == "__main__":
#    main()
