#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

void SelectionSort(vector<int>& A){
    int len = A.size();
    int sorted = 0;
    for(int i = 0; i < len-1; i++){
        int max = A[i];
        int max_ind = i;
        for(int j = sorted; j < len; j++){
            if(A[j] > max){
                max = A[j];
                max_ind = j;
            }
        }
        if(max_ind != i){
            int temp = A[i];
            A[i] = A[max_ind];
            A[max_ind] = temp;
        }
        sorted += 1;
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
    SelectionSort(v);
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
}
