#!/bin/bash

BIN_CAT=/bin/cat

echo ""

./build_products/appPE 2> build_products/error_log

if [ -a build_products/error_log ]
then
    echo -e "\nSome errors ocured. Error log created!"
    $BIN_CAT build_products/error_log
fi
echo ""
