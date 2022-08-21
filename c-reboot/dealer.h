#ifndef DEALER_H
#define DEALER_H

#include <iostream>
#include <cstdlib>
#include <string>
#include <map>

using namespace std;

/*
Deck of cards simulator

Public class member:
    string draw(int&):
        Pre:    Parameter - integer, passed by reference
        Post:   Returns - string
                Parameter - integer, passed by reference
*/

namespace dealer {

class Dealer {
    private:
        const int MAXVALUE = 13;
        const int MINVALUE = 1;
        int newCard;
        int countCards = 52;
        // Requires g++ -std=c++11 a2_sndbx.cpp
        map<int, int> deck = {{1,0}, {2,0}, {3,0}, {4,0}, {5,0}, {6,0}, {7,0}, {8,0}, {9,0}, {10,0}, {11,0}, {12,0}, {13,0}};
        map<int, string> display = {{1, "A"}, {11, "J"}, {12, "Q"}, {13, "K"}};
    public:
        string draw(int&);
};

}

#endif