#include <iostream>
#include <cstdlib>
#include <ctime>
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
unsigned long long int inputToInt(int&);

const int MAXVALUE = 10;
const int MINVALUE = 1;

int main() {

    int nullString = 0;
    unsigned long long int seed = inputToInt(nullString);  

    // srand is seeded globally
    if (nullString)
        srand(time(0)); 
    else
        srand(seed);


    
    int total = 0;
    int firstCard;
    int currentCard;

    firstCard = dealer();
    currentCard = dealer();
    total = firstCard + currentCard;
    
    printf("First cards: %d, %d\n", firstCard, currentCard);
    printf("Total: %d\n", total);

    // do {
    //     printf("Do you want another card? (y/n): ");

    // }
    // while()


    return 0;

}




int dealer() {
    return (rand() % (MAXVALUE - MINVALUE + 1)) + MINVALUE;
}


unsigned long long int inputToInt(int &nullString) {

    unsigned long long int output = 0;
    string userStr = "";

    printf("Input one of the following options:\n\t• Input integer for seeded randomizer (19-digit max)\n\t• Press [enter] for non-deterministic randomizer: ");    

    for (;;){

        userStr = "";
        getline(cin, userStr); 
        cin.clear();

        if (userStr.compare("") == 0) {
            userStr = "0";
            nullString = 1;
            break; 
        }      
        else {
            int checkInt = 1;
            for (int i = 0; i < userStr.length(); i++) {
                if (!(isdigit(userStr[i]) || userStr[i] == '\0')) {
                    printf("%c is not an integer. ", userStr[i]);
                    checkInt = 0;
                }
            }
            if (checkInt){
                break;
            }
            else {
                cout << "Please input a valid positive integer: ";
            }  
        } 
    }
    output = stoull(userStr, nullptr, 10);
    return output;
}
