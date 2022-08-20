#include <iostream>
#include <cstdlib>
#include <ctime>
#include <ios>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
#include <typeinfo>

#define PRINT_NAME(x) cout << #x << " - " << typeid(x).name() << '\n'

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
char* inputCheck(int &);

const int MAXVALUE = 10;
const int MINVALUE = 1;

int main() {


    char* seed = nullptr;    
    int length;

    printf("Input integer for seeded randomizer or press [enter] for non-deterministic randomizer: ");

    seed = inputCheck(length);  

    unsigned long long int seedling = 0;

    if (strcmp(seed, "") == 0) {
        srand(time(0));  
    }      
    else {
        seedling = strtoull(seed, nullptr, 10);
        srand(seedling);
    }

    cout << "****************" << endl;

    cout << length << endl;
    cout << "Type: " << typeid(seedling).name() << endl;
    cout << "Size of: " << sizeof(seedling) << endl;
    cout << "Seed value: " << seed << endl;
    printf("Value: %llu\n", seedling); 

    PRINT_NAME(unsigned long long int);

    cout << "****************" << endl;

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

    delete [] seed;  // I
	seed = nullptr;


    return 0;

}



int dealer() {
    return (rand() % (MAXVALUE - MINVALUE + 1)) + MINVALUE;
}


// Caller required to use "delete [] seed" for the pointer that is
// returned from this function.
char* inputCheck(int &length) {

    char* seed = nullptr;

    for (;;){

        string seedNum = "";
        getline(cin, seedNum); 
        cin.clear();
        length = seedNum.size();
        // Data verification purposes only //
        printf("Raw input: %s\n", seedNum.c_str());
        printf("Input length: %d\n", length);
        //////////////
        seed = new char[length + 1];
        strcpy(seed, seedNum.c_str()); // c_str() includes a \0
        
        int checkInt = 1;
        for (int i = 0; i < strlen(seed); i++) {
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
            for (int j=0; j<strlen(seed); j++) {
                seed[j] = '\0';  // Double quotes are strings, not char
            }
        }   
    }
    return seed;
}

