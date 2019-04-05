# -*- coding: utf-8 -*-
# try something like
def update():
#    prejoined  = db.UFO_table.id < 10
    joined = (db.UFO_table.GeoLocation == db.Location_table.GeoLocation)# & prejoined
    fields = (db.UFO_table.id, db.UFO_table.datetime, db.UFO_table.GeoLocation, db.UFO_table.shape, db.UFO_table.duration_sec, db.Location_table.city, db.Location_table.state, db.Location_table.country )
#    joined = db(db.executesql('select * from UFO_table LIMIT 10'))
    ufo_grid = SQLFORM.grid(query=joined, fields = fields, user_signature = False)
    met_grid = SQLFORM.smartgrid(db.Meteorite_table, user_signature = False)
    return locals()
