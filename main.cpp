
/********************************************************
*                                                       *
*  Project: PythonExercise                              *
*  Author: Michał Walczak                               *
*  Version: "1.1"                                       *
*  Last modified: 2016.10.20                            *
*  Status: initial draft                                *
*                                                       *
********************************************************/

#include <sstream>
#include <fstream>
#include <map>
#include <string>
#include <memory>
#include <vector>
#include "appPE.hpp"

int main(int argc, char* argv[])
{
    if(argc != 2)
    {
        std::cerr << "Error. Wrong number of arguments!\n";
        return 1;
    }
    else
    {
        std::string filename(argv[1]);
        assesorClass assesorObj;
        if(assesorObj.fileSizeCheck(filename) > assesorObj.maxFileSize)
        {
            std::cerr << "Error. Exceeded max file size" << std::endl;
            return 1;
        }
        return assesorObj.readFileContent(filename);
    }
}
