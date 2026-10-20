#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> queue(n);
    for (int& x : queue) 
        cin >> x;
        
    stack<int> deadend;
    int next_wagon = 1;
    for(int i = 0; i < n; i++){
        if(queue[i] == next_wagon)
            next_wagon++;
        else
            deadend.push(queue[i]);
        while (!deadend.empty()){
            if(deadend.top() == next_wagon){
                deadend.pop();
                next_wagon++;
            } else 
                break;
        }
    }

    if(next_wagon == n+1)
        cout << "YES";
    else
        cout << "NO";
    return 0;
}