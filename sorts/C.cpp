#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

void BubbleSort(vector<int>& A){
    int len = A.size();
    for(int i = 0; i < len-1; i++){
        bool sorted = true;
        for(int j = 0; j < len-i-1; j++){
            if(A[j] < A[j+1]){
                int temp = A[j+1];
                A[j+1] = A[j];
                A[j] = temp;
                sorted = false;
            }
        }
        if(sorted) break;
    }
}

int main() {
    vector<int> v;
    string line;
    getline(cin, line);

    stringstream ss(line);
    int x;
    while (ss >> x) {
        v.push_back(x);
    }
    BubbleSort(v);
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
}
