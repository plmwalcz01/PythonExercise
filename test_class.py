from email.mime import nonmultipart

from settings import SettingsClass
from pprint import pprint


settings_obj = SettingsClass()


class TestClass():
    def __init__(self):
        pprint(settings_obj.settings)
        no_incorr = settings_obj.too_few_words
        print(no_incorr, type(no_incorr))