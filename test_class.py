import test_files_generators as gen
from subprocess import Popen, PIPE
from settings import SettingsClass
from rapport_maker import RapportMaker


class TestClass:
    def __init__(self, settings, app_name, verbose):
        self.settings_obj = SettingsClass(json_settings=settings)
        self.rapport_maker = RapportMaker(app_name, verbose)
        self.app_name = app_name
        self.test_gens = []
        self.generate_tests()

    def run_tests(self):
        for tests in self.test_gens:
            for test in tests:
                out, err = Popen([self.app_name, test], stdout=PIPE, stderr=PIPE, universal_newlines=True).communicate()
                self.rapport_maker.add_test_output(test, err)
        self.rapport_maker.create_rapport_file()


    def generate_tests(self):
        print("generating tests...")
        for test_name, test_case in self.settings_obj.test_cases.items():
            self.test_gens.append(
                 gen.test_file_gen(self.settings_obj.test_files_path, test_name,
                                   test_case.get("number_of_tests", self.settings_obj.defaults["number_of_tests"]),
                                   test_case.get("min_number_of_words", self.settings_obj.defaults["min_number_of_words"]),
                                   test_case.get("max_number_of_words", self.settings_obj.defaults["max_number_of_words"]),
                                   test_case.get("min_word_size", self.settings_obj.defaults["min_word_size"]),
                                   test_case.get("max_word_size", self.settings_obj.defaults["max_word_size"]),
                                   test_case.get("1st_uppercase", self.settings_obj.defaults["1st_uppercase"])))