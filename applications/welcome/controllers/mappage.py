# -*- coding: utf-8 -*-
# try something like

import geopy.distance

session.testing = 0

def map():
    #these two variables will eventually be set by user
    coords_start = (29.8830556, -97.9411111)
    radius = 100

    coord_rows = db.executesql('select distinct u.id, l.GeoLocation from UFO_table u, Location_table l where u.GeoLocation = l.GeoLocation and l.country = "us" and l.state != "pr" LIMIT 1000')

    test = []
    for rows in coord_rows:
        if geopy.distance.vincenty(coords_start, rows[1] ).mi < radius:
            test.append(rows)


    test = session.testing
    row = db(db.Location_table.country == "us").select(db.Location_table.state, groupby=db.Location_table.state)

    return locals()





    #############################################################

def chooseState(selt, **post):
    print post

def incSession():
    session.testing += 1
    redirect(URL('mappage', 'map'))
