#coding: utf-8
import re
#from types import NoneType
from BeautifulSoup import BeautifulSoup
import requests
from LittleNuGa.model.proposal import Proposal

__author__ = 'tea'


class Parser(object):
    def load_and_parse(self):
        self.parse(self.load())

    def load(self):
        return requests.get(url='http://fl.ru').text

    def parse(self, x):

        resp_soup = BeautifulSoup(x)

        for tag in resp_soup.findAll('div', {'class': re.compile(r'.*\bb-post\b.*')}):
            print '---------'
            title_tag = tag.find('h2', {'class': re.compile(r'.*\bb-post__title\b.*')})
            name = title_tag.find('a').contents[0]
            ref = title_tag.find('a')['href']
            str_price = tag.find('script').string
            price = self.get_price(str_price)
            str_descr = str_price.findNext('script').string
            descr = self.get_descr(str_descr)
            str_stuff = str_descr.findNext('script').string
            stuff = self.get_stuff(str_stuff)
            proposal_example = Proposal(name, descr, price, stuff, ref)
            print proposal_example.to_json()

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
                    return descr
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
                return price.replace('&nbsp;', '')
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
                    return stuff
                stuff = ''

            else:
                i += 1