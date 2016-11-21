from setuptools.command import test

import test_files_generators as gen
from subprocess import call
from settings import SettingsClass


class TestClass():
    def __init__(self, settings):
        self.settings_obj = SettingsClass(json_settings=settings)
        self.test_gens = []
        self.generate_tests()

    def run_tests(self):
        for tests in self.test_gens:
            for test in tests:
                call(["./build_products/appPE", test])

    def generate_tests(self):
        print("generating tests...")
        for test_name, test_case in self.settings_obj.test_cases.items():
            self.test_gens.append(
                 gen.test_file_gen(self.settings_obj.test_files_path, test_name,
                                   test_case.get("number_of_tests", self.settings_obj.defaults["number_of_tests"]),
                                   test_case.get("max_number_of_words", self.settings_obj.defaults["max_number_of_words"]),
                                   test_case.get("max_word_size", self.settings_obj.defaults["max_word_size"]),
                                   test_case.get("1st_uppercase", self.settings_obj.defaults["1st_uppercase"])))