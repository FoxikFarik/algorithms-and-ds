#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

void CountSort(vector<int>& A){
    int len = A.size();
    vector<int> counts(101);
    for(int i = 0; i < len; i++)
        counts[A[i]]++;
    A.clear();
    for(int i = 0; i < 101; i++)
        for(int j = 0; j < counts[i]; j++)
            A.push_back(i);
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
    CountSort(v);
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
}