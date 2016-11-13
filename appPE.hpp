/********************************************************
*                                                       *
*  Project: PythonExercise                              *
*  Author: Michał Walczak                               *
*  Version: "1.1"                                       *
*  Last modified: 2016.10.20                            *
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
    const int minWords = 1;
    const int maxWordSize = 15;
    const int minWordSize = 1;
    assesorClass();

    void  showInputContent();
    int assesContent();
    int fileSizeCheck(const std::string filename);
    int readFileContent(const std::string filename);

    std::vector<std::string> mInput;
};

#endif /* APPPE_HPP_ */
