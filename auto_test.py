from test_class import TestClass

'./build_products/appPE'
if __name__ == '__main__':
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-s', '--settings', default='config/default_settings.json',
                            help='option allows to use custom test settings')
    arg_parser.add_argument('-v', '--verbose',action="store_true", dest="verbose", default=False, help='option to generate verbose rapport')
    arg_parser.add_argument('-a', '--app', required=True,
                            help='path to application to be tested')
    args = arg_parser.parse_args()
    print("Running settings", args.settings)
    test = TestClass(args.settings, args.app, args.verbose)
    test.run_tests()

