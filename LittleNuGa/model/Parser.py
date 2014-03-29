#coding: utf-8
import re
#from types import NoneType
from BeautifulSoup import BeautifulSoup
import requests

__author__ = 'tea'


class Parser(object):
    def load_and_parse(self):
        self.load()
        self.parse()

    def load(self):
        return requests.get(url='http://fl.ru').text

    def parse(self, x):

        resp_soup = BeautifulSoup(x)

        for tag in resp_soup.findAll('div', {'class': re.compile(r'.*\bb-post\b.*')}):
            title_tag = tag.find('h2', {'class': re.compile(r'.*\bb-post__title\b.*')})
            name = title_tag.find('a').contents[0]
            ref = title_tag.find('a')['href']
            #Proposal(name, descr, price, str_stuff, ref).name = name
            print ref
            str_price = tag.find('script').string
            self.get_price(str_price)
            str_descr = str_price.findNext('script').string
            self.get_descr(str_descr)
            str_stuff = str_descr.findNext('script').string
            self.get_stuff(str_stuff)

    def get_descr(self, str_descr):
        i = 0
        count = 0
        descr = ''

        while i < len(str_descr):
            if str_descr[i] == '>':
                i += 1
                count += 1
                if count == 2:
                    while str_descr[i] != '<':
                        descr = descr + str_descr[i]
                        i += 1
                    print 'descr = ', descr
                    break
            else:
                i += 1
        return descr

    def get_price(self, str_price):
        i = 0
        price = ''

        while i < len(str_price):
            if str_price[i] == '>':
                i += 1
                while str_price[i] != '<':
                    price = price + str_price[i]
                    i += 1
                print 'price = ',price.replace('&nbsp;', '')
                break
            else:
                i += 1
        return price

    def get_stuff(self, str_stuff):
        i = 0
        stuff = ''
        while i < len(str_stuff):
            if ord(str_stuff[i]) > 122 or 47 < ord(str_stuff[i]) < 58:
                while ord(str_stuff[i]) > 122 or ord(str_stuff[i]) == 32 or 47 < ord(str_stuff[i]) < 59:
                    stuff = stuff + str_stuff[i]
                    i += 1
                if stuff != '11':
                    print stuff
                stuff = ''

            else:
                i += 1