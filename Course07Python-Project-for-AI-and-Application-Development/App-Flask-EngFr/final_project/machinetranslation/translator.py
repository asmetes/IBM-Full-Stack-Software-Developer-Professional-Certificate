"""
translator.py
Module for translating text between English and French.
"""
import json
import os
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French using MyMemoryTranslator.
    :param english_text: The English text to be translated.
    :return: The translated French text.
    """
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English using MyMemoryTranslator.
    :param french_text: The French text to be translated.
    :return: The translated English text.
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text
