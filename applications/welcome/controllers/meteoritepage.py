# -*- coding: utf-8 -*-
# try something like

if not session.met_index:
    session.met_index = 0

if not session.met_sort:
    session.met_sort = 'ID'

if not session.met_display_flash:
    session.met_display_flash = 'No'

if not session.met_filter_cat:
    session.met_filter_cat = 'ID'
    session.met_filter_text = ''

def meteorite():
    page_count = items_per_page
    index = session.met_index
    sort_selection = session.met_sort
    filter_category = session.met_filter_cat
    search_text = session.met_filter_text

    if session.met_display_flash == 'Yes':
        response.flash = 'That field is expecting an integer to be searched (no letters or symbols).'

    session.met_display_flash = 'No'

    if (filter_category == "ID") and (not search_text == ''):
        met_set = db(db.Meteorite_table.id == search_text)
    elif (filter_category == "Mass") and (not search_text == ''):
        met_set = db(db.Meteorite_table.mass == search_text)
    elif (filter_category == "Geo Location") and (not search_text == ''):
        met_set = db(db.Meteorite_table.GeoLocation.contains(search_text))
    elif (filter_category == "Name") and (not search_text == ''):
        met_set = db(db.Meteorite_table.name.contains(search_text))
    elif (filter_category == "Class") and (not search_text == ''):
        met_set = db(db.Meteorite_table.class_met.contains(search_text))
    elif (filter_category == "Year Seen") and (not search_text == ''):
        met_set = db(db.Meteorite_table.year_seen == search_text)
    else:
        met_set = db(db.Meteorite_table)

    count = met_set.count()
    if count > 1000:
        count = 1000

    # Currently only selecting a MAX of 1000 rows (Takes a LONG time if we grab everything right now).

    if session.met_sort == 'ID':
        rows = met_set.select(orderby=db.Meteorite_table.id, limitby=(0,1000))
    elif session.met_sort == 'Mass':
        rows = met_set.select(orderby=db.Meteorite_table.mass, limitby=(0,1000))
    elif session.met_sort == 'Geo Location':
        rows = met_set.select(orderby=db.Meteorite_table.GeoLocation, limitby=(0,1000))
    elif session.met_sort == 'Name':
        rows = met_set.select(orderby=db.Meteorite_table.name, limitby=(0,1000))
    elif session.met_sort == 'Class':
        rows = met_set.select(orderby=db.Meteorite_table.class_met, limitby=(0,1000))
    elif session.met_sort == 'Year Seen':
        rows = met_set.select(orderby=db.Meteorite_table.year_seen, limitby=(0,1000))
    else:
        rows = met_set.select(orderby=db.Meteorite_table.id, limitby=(0,1000))
    return locals()

def next_page():
    session.met_index = session.met_index + items_per_page
    redirect(URL('meteorite'))


def prev_page():
    session.met_index = session.met_index - items_per_page
    redirect(URL('meteorite'))


def set_filter():
    session.met_index = 0
    if (request.vars.filter == 'ID' or request.vars.filter == 'Mass' or request.vars.filter == 'Year Seen') and request.vars.search_text != '':
        if request.vars.search_text.isdigit():
            session.met_filter_cat = request.vars.filter
            session.met_filter_text = request.vars.search_text
        else:
            session.met_display_flash = 'Yes'
    else:
        session.met_filter_cat = request.vars.filter
        session.met_filter_text = request.vars.search_text
    redirect(URL('meteorite'))


def reset_filter():
    session.met_index = 0
    session.met_filter_cat = None
    session.met_filter_text = ''
    redirect(URL('meteorite'))


def sort_met():
    session.met_index = 0

    if request.args(0) == 'A':
        session.met_sort = 'ID'
    elif request.args(0) == 'B':
        session.met_sort = 'Mass'
    elif request.args(0) == 'C':
        session.met_sort = 'Geo Location'
    elif request.args(0) == 'D':
        session.met_sort = 'Name'
    elif request.args(0) == 'E':
        session.met_sort = 'Class'
    elif request.args(0) == 'F':
        session.met_sort = 'Year Seen'
    redirect(URL('meteorite'))
