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
        self.test_gens.append(gen.correct_test_file_gen(self.settings_obj.number_of_correct_test_files, self.settings_obj.test_files_path))