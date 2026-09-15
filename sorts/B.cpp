#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

void InsertionSort(vector<int>& A){
    int len = A.size();
    for(int i = 1; i < len; i++){
        int temp = A[i];
        int j = i-1;
        while(j >=0 && A[j] > temp){
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = temp;
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
    InsertionSort(v);
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
}
