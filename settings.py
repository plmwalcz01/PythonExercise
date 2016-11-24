import json


class SettingsClass():
    def __init__(self, json_settings):
        self.settings_file = json_settings
        with open(json_settings) as data_file:
            self.settings = json.load(data_file)
            self.test_files_path = self.settings["test_files_path"]
            self.test_cases = self.settings["test_cases"]
            self.defaults = self.settings["default_test_values"]