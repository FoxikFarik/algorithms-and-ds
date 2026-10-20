#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int main(){
    deque<int> first_deck;
    deque<int> second_deck;
    for(int i = 0; i < 5; i++){
        int x;
        cin >> x;
        first_deck.push_back(x);
    }
    for(int i = 0; i < 5; i++){
        int x;
        cin >> x;
        second_deck.push_back(x);
    }

    int turns = 0;
    while(!first_deck.empty() && !second_deck.empty() && turns < 1000000){
        if(first_deck.front() > second_deck.front() && !(first_deck.front() == 9 && second_deck.front() == 0) || first_deck.front() == 0 && second_deck.front() == 9){
            int card = first_deck.front();
            first_deck.push_back(card);
            first_deck.pop_front();
            card = second_deck.front();
            first_deck.push_back(card);
            second_deck.pop_front();
        } else {
            int card = first_deck.front();
            second_deck.push_back(card);
            first_deck.pop_front();
            card = second_deck.front();
            second_deck.push_back(card);
            second_deck.pop_front();
        }
        turns++;
    }
    if(second_deck.empty())
        cout << "first" << " " << turns;
    else if(first_deck.empty())
        cout << "second" << " " << turns;
    else
        cout << "botva";
    return 0;
}