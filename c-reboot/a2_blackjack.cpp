#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <map>

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
int dealer(int&);
unsigned long long int inputToInt(int&);
string requestCard();

const int MAXVALUE = 13;
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

    firstCard = dealer(total);
    currentCard = dealer(total);
    
    printf("First cards: %d, %d\n", firstCard, currentCard);
    printf("Total: %d\n", total);

    string deal;
    int counter = 0;
    do {
        if (counter) {
            currentCard = dealer(total);
            printf("Card: %d\n", currentCard);
            printf("Total: %d\n", total);
        }

        if (total == 21) {
            cout << "Congratulations!" << endl;
            break;
        }
        else if (total > 21) {
            cout << "Bust!" << endl;
            break;
        }

        deal = requestCard();
        counter++;
    }
    while(deal == "y" || deal == "Y");

    cout << "Game Over" << endl;

    return 0;

}







unsigned long long int inputToInt(int &nullString) {

    unsigned long long int output = 0;
    string userStr = "";
    nullString = 0;

    printf("Input one of the following options:\n\t• Input integer for seeded randomizer (19-digit max)\n\t• Press [enter] for non-deterministic randomizer\nInput: ");    

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

    char* userCstr = nullptr;
    userCstr = new char[userStr.size() + 1];
    strcpy(userCstr, userStr.c_str());
    output = strtoull(userCstr, nullptr, 10); //Never throws exceptions
    delete [] userCstr;

    return output;
}


int dealer(int &total) {
    int newCard;
    int maxCard = 0;
    // Requires g++ -std=c++11 a2_sndbx.cpp
    map<int, int> deck = {{1,0}, {2,0}, {3,0}, {4,0}, {5,0}, {6,0}, {7,0}, {8,0}, {9,0}, {10,0}, {11,0}, {12,0}, {13,0}};
    do {
        newCard = (rand() % (MAXVALUE - MINVALUE + 1)) + MINVALUE;
        if (deck[newCard] > 4)
            maxCard = 1;
    } while(maxCard == 0);
    total += newCard;
    return newCard;
}


string requestCard() {
    string deal;
    int valid = 0;
    while (valid == 0) {
        printf("Do you want another card? (y/n): ");
        cin >> deal;
        if (deal[0] == 'y' || deal[0] == 'Y' || deal[0] =='N' || deal[0] == 'n') {
            if (deal.size() == 1)
                valid = 1;
            }
        if (deal == "n")
            break;
    }
    return deal;
}


