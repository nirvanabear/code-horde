#include <iostream>
#include <vector>

using namespace std;


/*
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a[1] >= a[2] <= a[3] >= a[4] <= a[5] ...


Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

    NOTE : If there are multiple answers possible, return the one that is lexicographically smallest.


Approaches:
    Swapping pairs
    [8,4,5,2,6,7,4]
    [5,8,4,2,4,6,7,6,5,3,5,6,6,3,3,5,3,2,2]
    8 > 5: swap
    4 < 5: swap
    2 > 5: no swap
    4 < 2: no swap
    6 > 4: swap
    7 < 4: swap

    Sort:
    then cut list in half and alternate back and forth
    

    Merge Sort:
    [8,4,5,2,6,7,4]
    [8,4,5,2] [6,7,4]
    [8,4][5,2][6,7][4]
    [8][4][5][2][6][7][4]

    [4,8][2,5][6,7][4]
    [2,4,5,8][4,6,7]
    [2,4,4,6,]

    ***
    [8,4]
    [8][4]

    ***

    Pseudocode:
    while vector size is > 1:
    Divide size of vector by 2
    Split array with index:
        0 to size / 2
        size / 2 + 1 to end
    Call merge_sort for each vector

    Compare vector 1 and 2:
        indexes i and j start at 0 and < vector size
        if vector1[i] < vector2[j]:
            add v1[i] to merge array
                increment i
            else add v2[j] to merge array
                increment j
        once one index has run out, add rest of other vector to array
        return merged array

            


*/

// vector<int> wave_vector(vector<int> nums) {

// }

vector<int> merge(vector<int> v1, vector<int> v2) {
    int g = 0;
    int h = 0;
    vector<int> merge;
    while (g < v1.size() & h < v2.size()) {
        if (v1[g] < v2[h]) {
            merge.push_back(v1[g]);
            g++;
        }
        else {
            merge.push_back(v2[h]);
            h++;
        }
    }
    if (g == v1.size()) {
        for (int i=h; i<v2.size(); i++) {
            merge.push_back(v2[i]);
        }
    }
    else {
        for (int j=g; j<v1.size(); j++) {
            merge.push_back(v1[j]);
        }
    }
    return merge;
}

vector<int> merge_sort(vector<int> data) {
    vector<int> v1;
    vector<int> v2;
    int i;
    if (data.size() > 1) {
        int split = data.size() / 2;
        for (i=0; i<split; i++) {
            v1.push_back(data[i]);
        }
        for (int j=i; j<data.size(); j++) {
            v2.push_back(data[j]);
        }
    }
    if (v1.size() > 1) {
        v1 = merge_sort(v1);
    }
    if (v2.size() > 1) {
        v2 = merge_sort(v2);
    }
    vector<int> output = merge(v1, v2);
    return output;
}


int main() {

    vector<int> v1 = {2,4,5,8};
    vector<int> v2 = {4,6,7};
    vector<int> result = merge(v1, v2);

    cout << endl;
    for (int r : result) {
        cout << r << ", ";
    }
    cout << endl;

    vector<int> data1 = {8,4,5,2,6,7,4};
    vector<int> merged1 = merge_sort(data1);
    for (int s : merged1) {
        cout << s << ", ";
    }
    cout << endl;

    return 0;
}
