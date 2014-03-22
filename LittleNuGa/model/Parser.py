#coding: utf-8
import re
from types import NoneType
from BeautifulSoup import BeautifulSoup
import requests

__author__ = 'tea'

class Parser(object):
    def load_and_parse(self):
        resp = requests.get(url = 'http://fl.ru')
        #print resp.text
        resp_soup = BeautifulSoup(resp.text)
        for tag in resp_soup.findAll('div', {'class': re.compile(r'.*\bb-post\b.*')}):
            title_tag = tag.find('h2', {'class': re.compile(r'.*\bb-post__title\b.*')})
            #if name is not NoneType:
                #name = name.get_text()
            name = title_tag.find('a').contents[0]
            ref = title_tag.find('a')['href']
            descr_tag = tag.find('div', {'class': re.compile(r'.*\bb-post__txt\b.*')})
            #descr_tag = tag.find('div')
            descr = descr_tag.contents

            print descr