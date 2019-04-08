# -*- coding: utf-8 -*-
# try something like

if not session.show_table:
    session.show_table = ''

def update():
    selection = session.show_table
#    prejoined  = db.UFO_table.id < 10
#    joined = (db.UFO_table.GeoLocation == db.Location_table.GeoLocation) & prejoined
#    fields = (db.UFO_table.id, db.UFO_table.datetime, db.UFO_table.GeoLocation, db.UFO_table.shape, db.UFO_table.duration_sec, db.Location_table.city, db.Location_table.state, db.Location_table.country )
#    joined = db(db.executesql('select * from UFO_table LIMIT 10'))
#    ufo_grid = SQLFORM.grid(query=joined, fields = fields, user_signature = False)
    ufo_grid = SQLFORM.grid(db.UFO_table, user_signature = False)
    met_grid = SQLFORM.grid(db.Meteorite_table, user_signature = False)
    loc_grid = SQLFORM.grid(db.Location_table, user_signature = False)
    return locals()

def table_to_show():
    if (request.vars.option == 'UFO'):
        session.show_table = 'ufo'
    elif (request.vars.option == 'MET'):
        session.show_table = 'met'
    elif (request.vars.option == 'LOC'):
        session.show_table = 'loc'
    redirect(URL('update'))
