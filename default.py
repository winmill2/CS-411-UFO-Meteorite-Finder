# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----

import autoUpdate

def index():
    #response.flash = T("put in a year (1990 t0 2017)")
    message = "Year not entered yet"
    row = ""
    if request.vars.sql_order:
        i = request.vars.sql_order

        try:
            year = int(i)
        except Exception:
            message = "bad value for year. Hit back and reenter."
            return message
        if year == 99999:
            #db.Meteorite_table.import_from_csv_file(open('met.csv','r'))
            #db.UFO_table.import_from_csv_file(open('final_ufo.csv','r'))
            x = autoUpdate.runUpdate(db)
            message = x#"pulled info"
            #db.Location_table.import_from_csv_file(open('location.csv','r'))
        elif year > 2013:
            message = "year is too high. Database only goes up to 2013 currently"
        elif year < 1939:
            message = "year is too low. Please input a year past 1938"

        else:
            message = "year is " + str(year)
            row = db(db.Meteorite_table.year_seen == year).select()

    return locals()

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki()

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
