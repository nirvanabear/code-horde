#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <regex>
#include <vector>
#include <unordered_map>
#include <typeinfo>

using namespace std;



/*
Author: Prakash Acharya

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

(A partially filled sudoku which is valid.)

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


Pseudocode:
    Validate each region in turn:
        Rows
        Columns
        Sub-boxes


        (how to iterate only one time through each row)
        (no repeats, no decimals, nothing over or under, correct length)

    if len of sudoku not equal 9, Fail

    For each in the sudoku:
        if len does not equal 9, Fail
        initialize new dictionary
        for each entry:
            pop from dict, with '' as default return value
                if returns anything but '' or '.', Fail
                if returns '', add to dict

    for index in range of list length
        initialize dictionary
        for each in sudoku
            pop list[index] from dict...

    BAD: Actually, I'm really liking setdefault for this, as it always
    returns a value, with no error option.


    for number1 0 through 2
        for number2 0 through 2
            initialize dictionary
            for index1 0 through 2, plus number1 (rows)
                for index2 0 through 2, plus number2 (columns)
                    pop list[index][index] from dict...
    
    Example:
        00 01 02 10 11 12 20 21 22

for numRow in range

0
0: 012
1: 012
2: 012

1
0: 345
1: 345
2: 345

2
0: 678
1: 678
2: 678

0
3: 012
4: 012
5: 012
*/


vector<vector<string> > import_text(string filepath) {
    fstream fileObject;
    string line;
    vector<vector<string> > table;
    vector<string> lineTote;
    regex validLine("\\[.*\\]");
    regex sudokuEnd("\\]");

    // Parses each incoming line and separates each sudoku
    // into its own vector.
    fileObject.open(filepath, ios::in);
    if (fileObject.is_open()) {
        while (getline(fileObject, line)) {
            if (line.empty()) break;
            if (regex_search(line, validLine)) {
                lineTote.push_back(line);
            }
            if (regex_match(line, sudokuEnd)) {
                table.push_back(lineTote);
                lineTote.clear();
            }
        }
        fileObject.close();
    }
    return table;
}


vector<vector<string> > cleanup_table(vector<vector<string> > table) {
    regex quoteBracket("'|\\[|\\]|\"|\\s");
    string editTote;
    for (int p=0; p<table.size(); p++) {
        for (int q=0; q<table[p].size(); q++) {
            editTote = regex_replace(table[p][q], quoteBracket, "");
            table[p][q] = editTote;
            // cout << "back: " << table[p][q].back() << endl;
            if (table[p][q].back() == ',') {
                table[p][q].pop_back();
            }
        }
    }
    return table;
}


vector<vector<vector<string> > > separate_elements(vector<vector<string> > table) {
    // TODO // why can't I instantiate stringstream stream; here??
    vector<vector<vector<string> > > matrix;
    vector<vector<string> > grid;
    vector<string> row;
    for (int t=0; t<table.size(); t++) {
        for (int u=0; u<table[t].size(); u++) {
            stringstream stream(table[t][u]);
            // cout << table[t][u] << endl;
            // stream << table[t][u];
            // stream.str(table[t][u]);
            while(stream.good()) {
                string element;
                getline(stream, element, ',');
                row.push_back(element);
            }
            grid.push_back(row);
            row.clear();
        }
        matrix.push_back(grid);
        grid.clear();
    }
    return matrix;
}


void print_table(vector<vector<string> > table) {
    for (int r=0; r<table.size(); r++) {
        cout << "Vector" << r << endl;
        for (int s=0; s<table[r].size(); s++) {
            cout << table[r][s] << endl;
        }
    }
    cout << endl;
}


void print_matrix(vector<vector<vector<string> > > matrix) {
    for (int f=0; f<matrix.size(); f++) {
        cout << "Vector" << f << endl;
        for (int g=0; g<matrix[f].size(); g++) {
            for (int h=0; h<matrix[f][g].size(); h++) {
                cout << "'" << matrix[f][g][h] << "'";
            }
            cout << endl;
        }
        cout << endl;
    }
    cout << endl;
}





bool check_rows(vector<vector<string> > sudoku) {
    for (int d=0; d<sudoku.size(); d++) {
        if (sudoku[d].size() != 9) {
            bool status = false;
            printf("Row %d failed.\n", d);
            return status;
        }
        int tableSize = sudoku[d].size() + (sudoku[d].size() / 3 + 1);
        unordered_map<char, int> hashTable;
        hashTable.reserve(tableSize);
        for (int e=0; e<sudoku[d].size(); e++) {
            if (isdigit(sudoku[d][e][0])) {
                // cout << typeid(sudoku[d][e][0]).name() << endl;
                if (hashTable.find(sudoku[d][e][0]) == hashTable.end()) {
                    hashTable.emplace(sudoku[d][e][0], 1);
                }
                else {
                    bool status = false;
                    printf("%c at %d, %d failed.\n", sudoku[d][e][0], d, e);
                    return status;
                }

            }
        }
    }
    bool status = true;
    return true;
}


bool check_columns(vector<vector<string> > sudoku) {
    if (sudoku.size() != 9) {
        cout << "Sudoku size failed." << endl;
        bool status = false;
        return status;
    }
    for (int v=0; v<sudoku[0].size(); v++) {
        int tableSize = sudoku.size() + (sudoku.size() / 3 + 1);
        unordered_map<char, int> hashTable;
        hashTable.reserve(tableSize);
        for (int w=0; w<sudoku.size(); w++) {
            if (isdigit(sudoku[w][v][0])) {
                if (hashTable.find(sudoku[w][v][0]) == hashTable.end()) {
                    hashTable.emplace(sudoku[w][v][0], 1);
                }
                else {
                    printf("%c at %d, %d failed.\n", sudoku[w][v][0], w, v);
                    bool status = false;
                    return status;
                }
            }
        }
    }
    bool status = true;
    return status;
}


bool check_blocks(vector<vector<string> > sudoku) {
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            int tableSize = sudoku.size() + (sudoku.size() / 3 + 1);
            unordered_map<char, int> hashTable;
            hashTable.reserve(tableSize);
            for (int k=i*3; k<(3+i*3); k++) {
                for (int l=j*3; l<(3+j*3); l++) {
                    if (isdigit(sudoku[k][l][0])) {
                        if (hashTable.find(sudoku[k][l][0]) == hashTable.end()) {
                            hashTable.emplace(sudoku[k][l][0], 1);
                        }
                        else {
                            printf("%c at %d, %d failed.\n", sudoku[k][l][0], k, l);
                            bool status = false;
                            return status;
                        }
                    }
                }
            }
        }
    }
    bool status = true;
    return status;
}


int main() {

    /**** Import from .txt file ****/
    string source_file = "sudokus.txt";
    vector<vector<string> > table = import_text(source_file);

    /**** Format incoming data ****/
    table = cleanup_table(table);
    print_table(table);
    vector<vector<vector<string> > > matrix = separate_elements(table);
    // print_matrix(matrix);

    /**** Validate Sudoku rows ****/
    for (int m=0; m<matrix.size(); m++) {
        bool rows_checked = check_rows(matrix[m]);
        printf("check_rows: %s\n", rows_checked ? "Passed" : "Failed");
        bool columns_checked = check_columns(matrix[m]);
        printf("check_columns: %s\n", columns_checked ? "Passed" : "Failed");
        bool blocks_checked = check_blocks(matrix[m]);
        printf("check_blocks: %s\n", columns_checked ? "Passed" : "Failed");
        if (!rows_checked | !columns_checked | !blocks_checked) {
            printf("Sudoku %d Invalid :(\n", m);
        }
        else {
            printf("Sudoku %d OK!\n", m);
        }
        cout << endl;
    }
    
    return 0;
}
