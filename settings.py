import json


class SettingsClass():
    def __init__(self, json_settings):
        self.settings_file = json_settings
        with open(json_settings) as data_file:
            self.settings = json.load(data_file)
            self.test_files_path = self.settings["test_files_path"]
            self.no_upper_case = self.settings["incorrect_test_files"]["no_upper_case"]
            self.too_few_words = self.settings["incorrect_test_files"]["too_few_words"]
            self.too_large_test_files = self.settings["incorrect_test_files"]["too_large_test_files"]
            self.too_long_words = self.settings["incorrect_test_files"]["too_long_words"]
            self.too_many_words = self.settings["incorrect_test_files"]["too_many_words"]
            self.too_short_words = self.settings["incorrect_test_files"]["too_short_words"]
            self.too_small_test_files = self.settings["incorrect_test_files"]["too_small_test_files"]
            self.number_of_correct_test_files = self.settings["number_of_correct_test_files"]
