#include <iostream>
#include <cstdlib>
#include <string>
#include <map>
#include "dealer.h"

using namespace std;



namespace dealer {

string Dealer::draw(int &total) {
    if (countCards <= 0) {
        return "Deck is empty.";
    }
    else {
        int maxCard = 0;
        string show;
        do {
            maxCard = 0;
            newCard = (rand() % (MAXVALUE - MINVALUE + 1)) + MINVALUE;
            deck[newCard] += 1;
            if (deck[newCard] > 4) {
                maxCard = 1;
                printf("No more %ds!\n", newCard);
            }
        } while(maxCard == 1);

        if (newCard == 1) {
            ace = 1;
        }
        if (newCard > 10)
            total += 10;
        else if (newCard == 1) {
            total += 11;
        }
        else
            total += newCard;
        if (ace == 1 && total > 21) {
            total -= 10;
            ace = 0; 
        }
    
    if (newCard < 2 || newCard > 10) {
        show = display[newCard];
    }
    else
        show = to_string(newCard);
    countCards--;
    return show;
    }
}

}

