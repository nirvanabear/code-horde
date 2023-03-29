
#include <vector>
#include <string>
#include <iostream>
#include <unordered_set>
#include <numeric>
#include "hash_table.h"
using namespace std;
using namespace hash_table;

/*
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Example 1:

Input: [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

*************

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.

Pseudocode1:
    Create hash table that is 1.3 times the size of the list
    Iterate through vector
        attempt to pop from hash map
            if unsuccessful, add to hash map with value of 1
    Return only remaining hash map entry

Pseudocode2:
    Start with 0
    Iterate through
        Bitwise & each to number
    Return number

*/


int main() {
    int nums[] = {4,1,2,1,2};
    int size = sizeof(nums) / sizeof(int);

    // Solution 1: Hash table
    int tableSize = size + (size / 3 + 1);  // 30% larger than n
    HashTable* hashTable = ht_create(tableSize);
    for (int i=0; i<size; i++) {
        string temp = to_string(nums[i]);
        if (!ht_pop(hashTable, temp.c_str())) {
            ht_insert(hashTable, temp.c_str(), 1);
        }
    }
    ht_print(hashTable);
    ht_delete(hashTable);

    // Solution 2: Bitwise
    int number = 0;
    for (int j=0; j<size; j++) {
        number ^= nums[j];
    }
    cout << "Bitwise answer: " << number << endl;

    // Solution 3: Difference of array sum vs. array set.
    unordered_set<int> numSet (nums, nums+size);
    int sum1 = accumulate(nums, nums+size, 0);
    int sum2 = accumulate(numSet.begin(), numSet.end(), 0);
    cout << "Set arithmetic answer: " << 2*sum2 - sum1 << endl;
    

    return 0;
}