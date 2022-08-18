#include <iostream>
#include <cstdlib>
#include <ctime>
#include <ios>
#include <limits>
#include <string>

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

//Function prototype
int dealer();
void inputCheck(char*);

const int LENGTH = 11;
const int MAXVALUE = 10;
const int MINVALUE = 1;

int main() {


    char seed[LENGTH] = "";    // Cannot be single quote
    // char* seed = nullptr;    // Same thing, just dynamic allocation
    // seed = new char[LENGTH];

    printf("Input integer for seeded randomizer or press enter for non-deterministic randomizer (10-digit max): ");
    
    inputCheck(seed);  

    if (strcmp(seed, "") == 0)
        cout << "Empty!" << endl;

    printf("String: %s \n", seed);

    unsigned int seedling;

    // No null char, only strings
    if (strcmp(seed, "") == 0) {
        seedling = strtoul(seed, NULL, LENGTH);
        srand(seedling);    
    }      
    else
        srand(time(0));

    printf("Integer: %u: \n", seedling);
    // cout << seedling << endl;
    cout << rand() << endl;


    int y;

    // Limits the range of the random number.
    while (0) {
        cin.get();
        // y = (rand() % (MAXVALUE - MINVALUE + 1)) + MINVALUE;
        y = dealer();
        cout << y;
    }

    
    int total = 0;
    int currentCard;
    int previousCard;

    currentCard = dealer();
    previousCard = currentCard;
    currentCard = dealer();
    total = currentCard + previousCard;
    
    printf("First cards: %d, %d\n", currentCard, previousCard);
    printf("Total: %d\n", total);

    // do {
    //     printf("Do you want another card? (y/n): ");

    // }
    // while()

    // delete [] seed;  // Also needed for dynamic alloca
	// seed = nullptr;

    return 0;

}





void inputCheck(char* seed) {

    // char* seed[LENGTH];
    for (;;){

        cin.get(seed, LENGTH, '\n');//Leaves \n in buffer for ignore
        cin.clear();  // Clears error flags
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        
        int checkInt = 1;
        for (int i = 0; i < LENGTH; i++) {
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
                seed[j] = '\0';  // Double quotes are strings, not char
            }
        }   
    }
}



int dealer() {
    return (rand() % (MAXVALUE - MINVALUE + 1)) + MINVALUE;
}