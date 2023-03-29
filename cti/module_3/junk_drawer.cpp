#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;


int main() {

    

    /**** Splits a quoteless string at each comma ****/
    // stringstream stream(rowStr);
    stringstream stream;
    stream << rowStr;
    while(stream.good()) {
        string element;
        getline(stream, element, ',');
        numList.push_back(element);
    }
    // for (int i=0; i<numList.size(); i++) {
    //     cout << numList[i];
    // }
    // cout << endl;


    /**** Sticks a vector in a vector and prints ****/
    vector_of_vectors1.push_back(numList);

    for (int i=0; i<vector_of_vectors1.size(); i++) {
        for (int j=0; j<vector_of_vectors1[i].size(); j++) {
            // cout << vector_of_vectors1[i][j];
            // cout << i << ", " << j << endl;
        }
    }



    

    // cosut << endl;
    // cout << "table size: " << vector_of_vectors1.size() << endl;
    // cout << "vector size: " << vector_of_vectors1[0].size() << endl;
    // cout << vector_of_vectors1[0][1] << endl;

}