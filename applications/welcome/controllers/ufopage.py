# -*- coding: utf-8 -*-
# try something like

if not session.ufo_index:
    session.ufo_index = 0

if not session.ufo_sort:
    session.ufo_sort = 'ID'

if not session.ufo_display_flash:
    session.ufo_display_flash = 'No'

if not session.ufo_filter_cat:
    session.ufo_filter_cat = 'ID'
    session.ufo_filter_text = ''

def ufo():
    page_count = items_per_page
    index = session.ufo_index
    sort_selection = session.ufo_sort
    filter_category = session.ufo_filter_cat
    search_text = session.ufo_filter_text

    if session.ufo_display_flash == 'Yes':
        response.flash = 'That field is expecting an integer to be searched (no letters, spaces, or symbols).'
    session.ufo_display_flash = 'No'

    if (filter_category == "ID") and (not search_text == ''):
        ufo_set = db(db.UFO_table.id == search_text)
    elif (filter_category == "Date Time Year") and (not search_text == ''):
        ufo_set = db(db.UFO_table.datetime.year() == search_text)
    elif (filter_category == "Date Time Month") and (not search_text == ''):
        ufo_set = db(db.UFO_table.datetime.month() == search_text)
    elif (filter_category == "Date Time Day") and (not search_text == ''):
        ufo_set = db(db.UFO_table.datetime.day() == search_text)
    elif (filter_category == "Geo Location") and (not search_text == ''):
        ufo_set = db(db.UFO_table.GeoLocation.contains(search_text))
    elif (filter_category == "Shape") and (not search_text == ''):
        ufo_set = db(db.UFO_table.shape.contains(search_text))
    elif (filter_category == "Comments") and (not search_text == ''):
        ufo_set = db(db.UFO_table.comments.contains(search_text))
    elif (filter_category == "Duration") and (not search_text == ''):
        ufo_set = db(db.UFO_table.duration_sec == search_text)
    else:
        ufo_set = db(db.UFO_table)

    count = ufo_set.count()


    if session.ufo_sort == 'ID':
        rows = ufo_set.select(orderby=db.UFO_table.id)
    elif session.ufo_sort == 'Date Time':
        rows = ufo_set.select(orderby=db.UFO_table.datetime)
    elif session.ufo_sort == 'Geo Location':
        rows = ufo_set.select(orderby=db.UFO_table.GeoLocation)
    elif session.ufo_sort == 'Shape':
        rows = ufo_set.select(orderby=db.UFO_table.shape)
    elif session.ufo_sort == 'Comments':
        rows = ufo_set.select(orderby=db.UFO_table.comments)
    elif session.ufo_sort == 'Duration':
        rows = ufo_set.select(orderby=db.UFO_table.duration_sec)
    else:
        rows = ufo_set.select(orderby=db.UFO_table.id)
    return locals()

def next_page():
    session.ufo_index = session.ufo_index + items_per_page
    redirect(URL('ufo'))


def prev_page():
    session.ufo_index = session.ufo_index - items_per_page
    redirect(URL('ufo'))


def set_filter():
    session.ufo_index = 0
    if (request.vars.filter == 'ID' or request.vars.filter == 'Duration' or request.vars.filter == 'Date Time Year'
        or request.vars.filter == 'Date Time Month' or request.vars.filter == 'Date Time Day') and request.vars.search_text != '':
        if request.vars.search_text.isdigit():
            session.ufo_filter_cat = request.vars.filter
            session.ufo_filter_text = request.vars.search_text
        else:
            session.ufo_display_flash = 'Yes'
    else:
        session.ufo_filter_cat = request.vars.filter
        session.ufo_filter_text = request.vars.search_text
    redirect(URL('ufo'))


def reset_filter():
    session.ufo_index = 0
    session.ufo_filter_cat = None
    session.ufo_filter_text = ''
    redirect(URL('ufo'))


def sort_ufo():
    session.ufo_index = 0

    if request.args(0) == 'A':
        session.ufo_sort = 'ID'
    elif request.args(0) == 'B':
        session.ufo_sort = 'Date Time'
    elif request.args(0) == 'C':
        session.ufo_sort = 'Geo Location'
    elif request.args(0) == 'D':
        session.ufo_sort = 'Shape'
    elif request.args(0) == 'E':
        session.ufo_sort = 'Comments'
    elif request.args(0) == 'F':
        session.ufo_sort = 'Duration'
    redirect(URL('ufo'))
