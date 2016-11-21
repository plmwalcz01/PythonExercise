/********************************************************
*                                                       *
*  Project: PythonExercise                              *
*  Author: Michał Walczak                               *
*  Version: "1.2"                                       *
*  Last modified: 2016.11.21                            *
*  Status: initial draft                                *
*                                                       *
********************************************************/

#include <iostream>
#include <vector>
#include <string>

#ifndef APPPE_HPP_
#define APPPE_HPP_

class assesorClass
{
public:
    const int maxFileSize = 100;
    const int maxWords = 10;
    const int minWords = 5;
    const int maxWordSize = 15;
    const int minWordSize = 5;
    assesorClass();

    void  showInputContent();
    int assesContent();
    int fileSizeCheck(const std::string filename);
    int readFileContent(const std::string filename);

    std::vector<std::string> mInput;
};

#endif /* APPPE_HPP_ */
