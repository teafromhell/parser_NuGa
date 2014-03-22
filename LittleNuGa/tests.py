import unittest
from django.test import TestCase

# Create your tests here.
from LittleNuGa.model.Parser import Parser


class Tests(unittest.TestCase):
    def test_parse(self):
        Parser().load_and_parse()
