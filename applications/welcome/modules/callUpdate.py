# -*- coding: utf-8 -*-
import urllib2

def main():
    contents = urllib2.urlopen("https://utahgroup.pythonanywhere.com/welcome/default/index?sql_order=99999").read()


if __name__ == "__main__":
    main()
