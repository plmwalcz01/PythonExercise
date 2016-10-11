
/********************************************************
*                                                       *
*  Project: PythonExercise                              *
*  Author: Michał Walczak                               *
*  Version: "1.0"                                       *
*  Last modified: 2016.10.11                            *
*  Status: initial draft                                *
*                                                       *
********************************************************/

#include <iostream>

int ArgParse(char* argv[])
{
    std::cout << "Parsing arguments\n";
    return 1;
}

int main(int argc, char* argv[])
{
    if(ArgParse(argv))
    {
        std::cerr << "Error. Not enough arguments\n";
        return 1;
    };
    return 0;
}
