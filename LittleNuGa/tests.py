import unittest
from django.test import TestCase

# Create your tests here.
from LittleNuGa.model.Parser import Parser


class Tests(unittest.TestCase):
    def test_parse(self):
        Parser().parse(self.load_index())

    def load_index(self):
        file = open('LittleNuGa/fl.html','r')
        return file.read()
