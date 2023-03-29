#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <ctype>
using namespace std;



vector<string> return_vector() {
    vector<string> empty_vector(9);
    return empty_vector;
}

int main() {
    vector<string> numList = return_vector();

    string hello = "Howdy";
    vector<vector<string> > table;
    vector<string> stringBox; 
    stringBox.push_back(hello);
    table.push_back(stringBox);
    cout << table.size() << endl;
    cout << table[0][0] << endl;
    stringBox.clear();
    cout << table[0][0] << endl;

    // string rowStr = "['8','3','.','.','7','.','.','.','.'],";
    // string rowStr2 = "['8','3','.','.','7','.','.','.','.'],";
    // stringstream stream;
    // stream << rowStr;
    // stream << rowStr2;
    // while(stream.good()) {
    //     string element;
    //     getline(stream, element, ',');
    //     numList.push_back(element);
    // }
    // for (int i=0; i<numList.size(); i++) {
    //     cout << numList[i];
    // }
    // cout << endl;


    // /**** Removes apostrophes and brackets ****/
    // string rowStr = "['8','3','.','.','7','.','.','.','.'],";
    // regex regexp("'|\\[|\\]");
    // string noApost = regex_replace(rowStr, regexp, "");
    // // cout << noApost << endl;


    //     /**** Splits a quoteless string at each comma ****/
    // // stringstream stream(rowStr);
    // stringstream stream;
    // stream << rowStr;
    // while(stream.good()) {
    //     string element;
    //     getline(stream, element, ',');
    //     numList.push_back(element);
    // }
    // for (int i=0; i<numList.size(); i++) {
    //     cout << numList[i];
    // }
    // cout << endl;


    // /**** Sticks a vector in a vector and prints ****/
    // vector_of_vectors1.push_back(numList);

    // for (int i=0; i<vector_of_vectors1.size(); i++) {
    //     for (int j=0; j<vector_of_vectors1[i].size(); j++) {
    //         // cout << vector_of_vectors1[i][j];
    //         // cout << i << ", " << j << endl;
    //     }
    // }

    string nine = "9";
    cout << "Digit: " << isdigit(nine) << endl;


    return 0;
}