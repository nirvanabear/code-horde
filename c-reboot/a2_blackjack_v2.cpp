#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <map>
#include "dealer.h"

using namespace std;
using namespace dealer;

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


    /* TODO //
        functions for hands

        Multiple rounds of hands

        How many decks??
        Burn card
        Place bet
        Deal one up to player
        Deal one down to dealer
        Deal one up to player
        Deal one up to dealer
        If dealer shows ace, 
            insurance bet option
            peek and if blackjack, everybody loses (excpt bjack)
        Players hand
            if blackjack, pay 3/2 bet
            hit 
                (cannot then split or double down)
            stand
            double down
                only one more card then double the bet
            surrender
                forfeit but keep half the money
            split
                doubles bet
                separate cards and deal a hand to first card
                deal hand to second card
                second split is possible
        */


// Constants
const int MAXVALUE = 13;
const int MINVALUE = 1;

//Function prototype
unsigned long long int inputToInt(int&);
string yesOrNo(char*);
void playersHand(int &, int &, int &, int &, Dealer &);
void dealersHand(int &, int &, int &, int &, int, int, int, Dealer &);
void outcomes(int, int, int, int, int, int);

int main() {

    int nullString = 0;
    unsigned long long int seed = inputToInt(nullString);  

    // srand is seeded globally
    if (nullString)
        srand(time(0)); 
    else
        srand(seed);

    Dealer pokerAlice;
    string keepPlaying;

    cout << "￦" << endl;


    do {
        int playerWinnings = 0;

        int total = 0;
        int blackjack = 0;
        int bust = 0;
        int bet = 0;

        playersHand(total, blackjack, bust, bet, pokerAlice);


        int dealerTotal = 0;
        int dealerBJack = 0;
        int dealerBust = 0;

        dealersHand(dealerTotal, dealerBJack, dealerBust, bet, bust, blackjack, total, pokerAlice);

        outcomes(total, dealerTotal, bust, dealerBust, blackjack, dealerBJack);

        char anotherHand[] = "Do you want to play again?";
        keepPlaying = yesOrNo(anotherHand);

    } while(keepPlaying == "y" || keepPlaying == "Y" || pokerAlice.deckCount() <= 0);

    cout << "￦" << endl;

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
                cout << "Please input a valid positive integer or press [enter]: ";
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


string yesOrNo(char* query) {
    string response;
    int valid = 0;
    while (valid == 0) {
        printf("%s (y/n): ", query);
        cin >> response;
        if (response[0] == 'y' || response[0] == 'Y' || response[0] =='N' || response[0] == 'n') {
            if (response.size() == 1)
                valid = 1;
            }
        if (response == "n")
            break;
    }
    return response;
}


void playersHand(int &total, int &blackjack, int &bust, int &bet, Dealer &pokerAlice) {

    total = 0;
    blackjack = 0;
    bust = 0;
    bet = 0;

    string firstCard;
    string currentCard;

    firstCard = pokerAlice.draw(total);
    currentCard = pokerAlice.draw(total);
    
    printf("First cards: %s, %s\n", firstCard.c_str(), currentCard.c_str());
    printf("Total: %d\n", total);

    if (total == 21) {
        blackjack = 1;
        cout << "Blackjack!" << endl;
    }

    string deal;
    int counter = 0;

    do {
        if (counter) {
            currentCard = pokerAlice.draw(total);
            printf("Card: %s\n", currentCard.c_str());
            printf("Total: %d\n", total);
        }

        if (total == 21) {
            cout << "Vingt-et-Un!" << endl;
            break;
        }
        else if (total > 21) {
            cout << "Bust!" << endl;
            bust = 1;
            break;
        }

        char anotherCard[] = "Do you want another card?";
        deal = yesOrNo(anotherCard);
        counter++;
    }
    while(deal == "y" || deal == "Y");

}


void dealersHand(int &dealerTotal, int &dealerBJack, int &dealerBust, int &bet, int bust, int blackjack, int total, Dealer &pokerAlice) {

    string firstCard;
    string currentCard;

    if (!bust) {

        cout << endl << "Dealer's Turn: " << endl << endl;
        cin.get();

        firstCard = pokerAlice.draw(dealerTotal);
        currentCard = pokerAlice.draw(dealerTotal);

        printf("Dealer's first cards: %s, %s\n", firstCard.c_str(), currentCard.c_str());
        printf("Dealer's total: %d\n", dealerTotal);
        cin.get(); 

        if (dealerTotal == 21) {
            dealerBJack = 1;
        }   

        while(dealerTotal < 17 && dealerTotal < total) {
                currentCard = pokerAlice.draw(dealerTotal);
                printf("Dealer's card: %s\n", currentCard.c_str());
                printf("Dealer's total: %d\n\n", dealerTotal);
                cin.get();

        }
        if (dealerTotal > 21) {
            dealerBust = 1;
            cout << "Dealer busts!" << endl;
        }
    }
}


void outcomes(int total, int dealerTotal, int bust, int dealerBust, int blackjack, int dealerBJack) {
    if ((dealerTotal > total && !dealerBust) || bust) {
        cout << "You Lose!" << endl;
    }
    else if (dealerTotal == total) {
        if (blackjack && dealerBJack) {
            cout << "Blackjack standoff!" << endl;
        }
        else if (blackjack) {
            cout << "Blackjack! You win!" << endl;
        }
        else if (dealerBJack) {
            cout << "Dealer's blackjack! You lose!" << endl;
        }
        else
            cout << "Standoff!" << endl;
    }
    else
        cout << "You win!" << endl;
}
