#include <iostream>
#include <cstdlib>
#include <ctime>
#include <ios>
#include <limits>
#include <string>
#include <sstream>

using namespace std;

/*
Understand: 	Analyze the problem statement
    Random 1-10 card generator, deals 2, then deals on command until
    user ends, total is 21 or total is over 21.
Match: 	 	Recall problems you have seen, determine similarities
Plan: 			Perform the steps, write them out, describe the process

    display option to input seed, or just press enter to use time random
        console out
        console in, but where to save?
            save to string
            getline?


    create negative seed int
    user option to input their own seed
    if seed non negative:
        random seeding gets that number
    else
        use random seeding with time
    random number generate twice
    display numbers
    track total
    create loop if not 21
        random number generator
        display number
        dislay total
        if 21, display win
            break
        if over 21, display loss
            break
        user option to break loop


Implement: 	Translate your plan to code
Review: 		Make sure your code works, handle corner cases
Evaluate: 		Determine time & space efficiency of solution
*/

const int LENGTH = 11;

int main(){

    char seed[LENGTH] = "";    // Cannot be single quote

    printf("Input integer for seeded randomizer or press enter for non-deterministic randomizer (10-digit max): ");
    
    for (;;){

        cin.get(seed, LENGTH, '\n'); // Leaves \n in buffer
        cin.clear();  // Clears error flags
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // needs \n
        
        int checkInt = 1;
        for (int i = 0; i < LENGTH; i++) {
            // cout << seed[i];
            if (!(isdigit(seed[i]) || seed[i] == '\0')) {
                printf("%c is not an integer. ", seed[i]);
                checkInt = 0;
            }
        }
        if (checkInt){
            break;
        }
        else {
            cout << "Please input a valid positive integer: ";
            for (int j=0; j<LENGTH; j++) {
                seed[j] = '\0';  // Double quotes are strings not char
            }
        }   
    }

    cout << "Out of loop!" << endl;

    if (strcmp(seed, "") == 0)
        cout << "Empty!" << endl;

    printf("Integer: %s \n", seed);
   
    // if (seed >= 0)
    //     srand(seed);
    // else
    //     srand(time(0));

    // cout << rand() << endl;
    // cout << time(0) << endl;
    // cout << time(nullptr) << endl;

    // // Limits the range of the random number.
    // // y = (rand() % (maxValue - minValue + 1)) + minValue;

    string input1 = "";
    // string input2 = "";
    // string input3 = "";
    // char input4[21];
    // // char single = "";




    // cin >> input4;
    // input2 = cin.get();
    // input3 = cin.get();

    stringstream myStream(input1);

    // if (input4 == "")
    //     cout << "Empty!" << endl;

    
    // cout << "input4:" << input4 << ":" << endl;
    // cout << "input1:" << input1 << ":" << endl;
    // cout << "input2:" << input2 << ":" << endl;
    // cout << "input3:" << input3 << ":" << endl;
    // cout << "Done." << endl;

    // cin >> seed;
    // cout << seed;

    return 0;
}