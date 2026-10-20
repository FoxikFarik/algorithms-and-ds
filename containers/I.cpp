#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> row(n);
    for (int& x : row) 
        cin >> x;

    int popped = 0;
    stack<int> balloons;
    for(int i = 0; i < n; i++){
        if(!balloons.empty())
            if(row[i] != balloons.top()){
                int target = balloons.top();
                int popped_local = 0;
                while(!balloons.empty()){
                    if(balloons.top() == target){
                        balloons.pop();
                        popped_local++;
                    } else
                        break;
                }
                if(popped_local >= 3)
                    popped += popped_local;
                else
                    for(int j = 0; j < popped_local; j++)
                        balloons.push(target);
            }
        balloons.push(row[i]);
    }

    cout << popped;
    return 0;
}