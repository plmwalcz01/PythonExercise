import os
from datetime import datetime

class RapportMaker:
    def __init__(self, app_name, verbose):
        self.app_name = app_name
        self.raw_rapport = []
        self.c_output = ""
        self.c_error = ""
        self.failed_tests = 0
        self.passed_tests = 0
        self.verbose = verbose

    def add_test_output(self, current_test, c_error):
        if str(c_error):
            self.raw_rapport.append("\n"+current_test+"\n")
            self.raw_rapport.append(str(c_error))
        if "error" in str(c_error).lower():
            self.failed_tests += 1
        else:
            self.passed_tests += 1

    def prepare_rapport(self):
        rapport = []
        bracket = "*" * 70 #random values that looks good
        separator_lines = "-" * 60 #random values that looks good
        rapport.append(bracket+"\n")
        rapport.append("\nTested {0} on {1}".format(self.app_name, str(datetime.now().strftime("%Y-%m-%d %H:%M"))))
        rapport.append("\nExecuted {0} test cases.".format(str(self.failed_tests + self.passed_tests)))
        rapport.append("\n{0} tests passed and {1} tests failed\n\n".format(self.passed_tests, self.failed_tests))
        rapport.append(bracket+"\n")
        if self.verbose:
            for line in self.raw_rapport:
                if "error" in line.lower():
                    rapport.append(line)
                else:
                    rapport.append("\n"+separator_lines+"\n")
                    rapport.append(line)
        rapport.append("\n"+bracket+"\n")
        return rapport

    def create_rapport_file(self):
        filename = 'build_products/rapport'
        try:
            test_file = open(filename, 'w')
        except (OSError, IOError) as e:
            print("Error:", e)
        formatted_rapport = self.prepare_rapport()
        test_file.writelines("%s" % rapport for rapport in formatted_rapport)
        test_file.close()