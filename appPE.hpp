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
    assesorClass();
    bool assesContent();
    const int maxFileSize = 50;
    void  showInputContent();
    int fileSizeCheck(const std::string filename);
    bool readFileContent(const std::string filename);
    std::vector<std::string> mInput;
};

#endif /* APPPE_HPP_ */
