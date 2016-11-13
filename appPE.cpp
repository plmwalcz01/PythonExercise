
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
#include <cctype>
assesorClass::assesorClass()
{
    std::cout << __FUNCTION__ << std::endl;
}

int assesorClass::readFileContent(const std::string filename)
{
    std::cout << __FUNCTION__ << std::endl;
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
    return assesContent();
}

void  assesorClass::showInputContent()
{
    std::cout << __FUNCTION__ << std::endl;
    for (const auto &in : mInput)
    {
        std::cout << in << std::endl;
    }
}

int  assesorClass::fileSizeCheck(const std::string filename)
{
    std::cout << __FUNCTION__ << std::endl;
    std::ifstream myTestFile(filename.c_str(),
                             std::ios_base::binary | std::ios_base::ate);
    if (myTestFile.is_open())
    {
        return myTestFile.tellg();
    }
    else
    {
        std::cerr << "Error. Could not open file!";
        return 0;
    }
}

int assesorClass::assesContent()
{
    std::cout << __FUNCTION__ << std::endl;
    int result = 0;
    if(mInput.size() > maxWords)
    {
        std::cerr << "Error. File contains too many words!" << std::endl;
        result = 1;
    }
    else if(mInput.size() < minWords)
    {
        std::cerr << "Error. File contains no words!" << std::endl;
        result = 1;
    }
    else
    {
        std::cout << "File contains " << mInput.size() << " words" << std::endl;
    }

    for(const auto &line : mInput)
    {
        if(line.length() >= maxWordSize)
        {
            std::cerr << "Error in word: '" << line << "'. Word is too long! " << std::endl;
            result = 1;
        }
        else if(line.length() < minWordSize)
        {
            std::cerr << "Error in word: '" << line << "'. Word is too short! " << std::endl;
            result = 1;
        }
        if(!std::isupper(line.at(0)))
        {
            std::cerr << "Error in word: '" << line << "'. No upper case at the beginning!" << std::endl ;
            result = 1;
        }
    }
    return result;
}
