# -*- coding: utf-8 -*-
# try something like

import geopy.distance

if not session.state_id:
    session.state_id = 0
    session.stateName = ""

#session.testing = 0

def map():
    #these two variables will eventually be set by user
#     coords_start = (29.8830556, -97.9411111)
#     radius = 100

#     coord_rows = db.executesql('select distinct u.id, l.GeoLocation from UFO_table u, Location_table l where u.GeoLocation = l.GeoLocation and l.country = "us" and l.state != "pr" LIMIT 1000')

#     test = []
#     for rows in coord_rows:
#         if geopy.distance.vincenty(coords_start, rows[1] ).mi < radius:
#             test.append(rows)


#    test = session.testing
#    row = db(db.Location_table.country == "us").select(db.Location_table.state, groupby=db.Location_table.state)


#TODO: get sId being passed from view, format output, refresh div on click

    sId = session.state_id
    stateName = session.stateName
    sTxt = ""

    if int(sId) != 0:
        if int(sId) == 1:
            sTxt = 'al'
            stateName = "Alabama"
        elif int(sId) == 4:
            sTxt = 'az'
            stateName = "Arizona"
        elif int(sId) == 5:
            sTxt = 'ar'
            stateName = "Arkansas"
        elif int(sId) == 6:
            sTxt = 'ca'
            stateName = "California"
        elif int(sId) == 8:
            sTxt = 'co'
            stateName = "Colorado"
        elif int(sId) == 9:
            sTxt = 'ct'
            stateName = "Conneticut"
        elif int(sId) == 10:
            sTxt = 'de'
            stateName = "Delware"
        elif int(sId) == 12:
            sTxt = 'fl'
            stateName = "Florida"
        elif int(sId) == 13:
            sTxt = 'ga'
            stateName = "Georgia"
        elif int(sId) == 16:
            sTxt = 'id'
            stateName = "Idaho"
        elif int(sId) == 17:
            sTxt = 'il'
            stateName = "Illinois"
        elif int(sId) == 18:
            sTxt = 'in'
            stateName = "Indiana"
        elif int(sId) == 19:
            sTxt = 'ia'
            stateName = "Iowa"
        elif int(sId) == 20:
            sTxt = 'ks'
            stateName = "Kansas"
        elif int(sId) == 21:
            sTxt = 'ky'
            stateName = "Kentucky"
        elif int(sId) == 22:
            sTxt = 'la'
            stateName = "Louisiana"
        elif int(sId) == 23:
            sTxt = 'me'
            stateName = "Maine"
        elif int(sId) == 24:
            sTxt = 'md'
            stateName = "Maryland"
        elif int(sId) == 25:
            sTxt = 'ma'
            stateName = "Massachusetts"
        elif int(sId) == 26:
            sTxt = 'mi'
            stateName = "Michigan"
        elif int(sId) == 27:
            sTxt = 'mn'
            stateName = "Minnesota"
        elif int(sId) == 28:
            sTxt = 'ms'
            stateName = "Mississippi"
        elif int(sId) == 29:
            sTxt = 'mo'
            stateName = "Missouri"
        elif int(sId) == 30:
            sTxt = 'mt'
            stateName = "Montana"
        elif int(sId) == 31:
            sTxt = 'ne'
            stateName = "Nebraska"
        elif int(sId) == 32:
            sTxt = 'nv'
            stateName = "Nevada"
        elif int(sId) == 33:
            sTxt = 'nh'
            stateName = "New Hampshire"
        elif int(sId) == 34:
            sTxt = 'nj'
            stateName = "New Jersey"
        elif int(sId) == 35:
            sTxt = 'nm'
            stateName = "New Mexico"
        elif int(sId) == 36:
            sTxt = 'ny'
            stateName = "New York"
        elif int(sId) == 37:
            sTxt = 'nc'
            stateName = "North Carolina"
        elif int(sId) == 38:
            sTxt = 'nd'
            stateName = "North Dakota"
        elif int(sId) == 39:
            sTxt = 'oh'
            stateName = "Ohio"
        elif int(sId) == 40:
            sTxt = 'ok'
            stateName = "Oklahoma"
        elif int(sId) == 41:
            sTxt = 'or'
            stateName = "Oregon"
        elif int(sId) == 42:
            sTxt = 'pa'
            stateName = "Pennsylvania"
        elif int(sId) == 44:
            sTxt = 'ri'
            stateName = "Rhode Island"
        elif int(sId) == 45:
            sTxt = 'sc'
            stateName = "South Carolina"
        elif int(sId) == 46:
            sTxt = 'sd'
            stateName = "South Dakota"
        elif int(sId) == 47:
            sTxt = 'tn'
            stateName = "Tennessee"
        elif int(sId) == 48:
            sTxt = 'tx'
            stateName = "Texas"
        elif int(sId) == 49:
            sTxt = 'ut'
            stateName = "Utah"
        elif int(sId) == 50:
            sTxt = 'vt'
            stateName = "Vermont"
        elif int(sId) == 51:
            sTxt = 'va'
            stateName = "Virginia"
        elif int(sId) == 53:
            sTxt = 'wa'
            stateName = "Washington"
        elif int(sId) == 54:
            sTxt = 'wv'
            stateName = "West Virginia"
        elif int(sId) == 55:
            sTxt = 'wi'
            stateName = "Wisconsin"
        elif int(sId) == 56:
            sTxt = 'wy'
            stateName = "Whyoming"

#    state_rows = db.executesql('select distinct u.datetime, u.shape, u.duration_sec from UFO_table u, Location_table l where u.GeoLocation = l.GeoLocation and l.state = "az" order by u.datetime LIMIT 10')
    count = 0
    metcount = 0
    if int(sId) != 0:
        query = "select distinct u.datetime, u.shape, u.duration_sec, l.city, u.comments from UFO_table u, Location_table l where u.GeoLocation = l.GeoLocation and l.state = '%s' order by u.datetime" %(sTxt)
        metquery = "select distinct m.year_seen, m.name, m.class_met from Meteorite_table m, Location_table l where m.GeoLocation = l.GeoLocation and m.year_seen > 1800 order by m.year_seen limit 1000" # and l.state = '%s' order by m.year_seen" %(sTxt)

#TODO: Fix location table so each geo-location is associated w/ city, state, country
#REAL QUERY:     metquery = "select distinct m.year_seen, m.name, m.class_met l.city from Meteorite_table m, Location_table l where m.GeoLocation = l.GeoLocation and l.state = '%s' order by m.year_seen" %(sTxt) 
        state_rows = db.executesql(query)
       
        states = []

        for rows in state_rows:
            states.append(rows)
            count += 1
            
        mets = []
        met_rows = db.executesql(metquery)
        for rows in met_rows:
            mets.append(rows)
            metcount += 1

    else:
        states = []
        mets = []

    return locals()



    #############################################################

def chooseState(selt, **post):
    print post

def incSession():
    session.testing += 1
    redirect(URL('mappage', 'map'))
