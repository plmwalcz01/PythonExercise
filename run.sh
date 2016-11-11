#!/bin/bash

FIRST_ARG=$1
BIN_CAT=/bin/cat
BIN_RM=/bin/rm
ERROR_LOG_FILE=error_log
TEST_APP_FILE=appPE
BUILD_PATH=build_products
ERR_LOG=$BUILD_PATH/$ERROR_LOG_FILE
APP=$BUILD_PATH/$TEST_APP_FILE


echo "error log path :" $ERR_LOG
echo "app file path: " $APP

$BIN_RM $ERR_LOG 
/bin/ls $BUILD_PATH

./$APP $FIRST_ARG 2> $ERR_LOG
RETURN_VALUE=$?
echo "$RETURN_VALUE <-- result of running $APP with $FIRST_ARG"
if [ $RETURN_VALUE -eq 0 ]
then
    echo "All is well in the wonderland"
else
    echo -e "\nSome errors ocured. Error log created!"
    $BIN_CAT $ERR_LOG
fi
echo ""
