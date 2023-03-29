#include <iostream>
#include <string>
#include <sstream>
#include <regex>
#include <vector>
#include <unordered_map>
#include "hash_table.h"


using namespace std;
using namespace hash_table;


// #include <numeric>
// #include <fstream>


int main() {

    vector<vector<string> > broken;
    regex validLine("\\[.*\\]");
    regex sudokuEnd("\\]");

    string line = "Why???";
    regex_search(line, validLine);

    int tableSize = 10;
    HashTable* hashTable = ht_create(tableSize);
    string letters = "Hello";
    // string number = to_string(tableSize);
    ht_insert(hashTable, letters.c_str(), 1);
    cout << "test8" << endl;
}