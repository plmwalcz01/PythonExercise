import os, sys

from test_class import TestClass

def redirect_stdout():
    print("Redirecting stdout")
    sys.stdout.flush() # <--- important when redirecting to files

    # Duplicate stdout (file descriptor 1)
    # to a different file descriptor number
    newstdout = os.dup(1)

    # /dev/null is used just to discard what is being printed
    raport = os.open('build_products/raport', os.O_WRONLY)

    # Duplicate the file descriptor for /dev/null
    # and overwrite the value for stdout (file descriptor 1)
    os.dup2(raport, 1)

    # Close devnull after duplication (no longer needed)
    os.close(raport)

    # Use the original stdout to still be able
    # to print to stdout within python
    sys.stdout = os.fdopen(newstdout, 'w')




if __name__ == '__main__':
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-s', '--settings', default='config/default_settings.json',
                            help='option allows to use custom test settings')
    args = arg_parser.parse_args()
    print("Running settings", args.settings)
    test = TestClass(args.settings)
    redirect_stdout()
    test.run_tests()

    # redirect_stdout()
    # call(["./build_products/appPE", "test",])
    # call(["./build_products/appPE", "test2", ])
    # call(["./build_products/appPE", "test3", ])
    # print("finished")

