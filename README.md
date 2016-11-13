# PythonExercise
The goal is to write a simple C++ app that takes command line input in form of input file name containing few words. Then based on that write python script that generates input file and runs the app 1000 times gathering app's output to stdout &amp;stderr to generate raport. Report is than saved in different file.

The exercise is to learn the basics of automated testing and put it into practice. 

Build applicaion and test results (raport) should be in build_products directory

Details about application:

Parameters:
Application takes 1 parameter which is filename of the file to be tested. 

Application Description:  
Application tests if test file exists and its size is less than 100bytes.
Then assesorClass object is created and following assesments are done:
- checking if test file contains from 1 to 10 words and if thats correct 
	  number of words is outputed
- checking if length of each word is between 1 and 15 characters long (15th char included)
- checking if first letter of each  word is upper case letter

Return Value:  
Application returns 0 on success (every assessment is passed) and 1 if any error occur or any assessment fails

Output:  
Application prints logs on stdout and error logs on stderr.

Example usage:

```sh  
$ ./build_products/appPE test
```  
- "appPE" is the application binary
- "test" is the filename to be tested
