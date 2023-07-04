import unittest
from translator import french_to_english,english_to_french

#Test Translator
class TestEnglishToFrench(unittest.TestCase):

    def test1(self):
        self.assertEqual(english_to_french('Good morning'), 'Bonjour') 
        self.assertEqual(english_to_french('boy'), 'garçon')   

    def test2(self):
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):

    
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('garçon'), 'boy')
    def test2(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Good morning')

unittest.main()