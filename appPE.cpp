
/********************************************************
*                                                       *
*  Project: PythonExercise                              *
*  Author: Michał Walczak                               *
*  Version: "1.1"                                       *
*  Last modified: 2016.10.20                            *
*  Status: initial draft                                *
*                                                       *
********************************************************/

#include "appPE.hpp"
#include <algorithm>
#include <fstream>
assesorClass::assesorClass()
{
}

bool assesorClass::readFileContent(const std::string filename)
{
    std::cout << "Processing file: " << filename << std::endl;

    std::ifstream myTestFile;
    std::string input_str;
    myTestFile.open(filename.c_str(), std::ios_base::in );
    if (myTestFile.is_open())
    {
        while (myTestFile >> input_str)
        {
            mInput.push_back(input_str);
        }
    }
    myTestFile.close();
    showInputContent();
    return true;
}

void  assesorClass::showInputContent()
{
    for (const auto &in : mInput)
    {
        std::cout << in << std::endl;
    }
}
    int  assesorClass::fileSizeCheck(const std::string filename)
{
    std::ifstream myTestFile(filename.c_str(),
                             std::ios_base::binary | std::ios_base::ate);
    return myTestFile.tellg();
}

bool assesorClass::assesContent()
{
    return false;
}
