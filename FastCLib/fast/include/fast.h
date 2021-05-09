#pragma once
#include <cstdint> // for std::int_fast64_t
#include <string.h>
#include <iostream>
#include <math.h>

extern "C"
{   
    std::string multiply(std::string lhs, std::string rhs);
    std::string subtract(std::string lhs, std::string rhs);
    std::string add(std::string lhs, std::string rhs);
    char *str_wrapper(char* lhs, char* rhs);
    unsigned long long mul(unsigned long& a, unsigned long& b);
    unsigned long long powint(int& a, int& b);
};