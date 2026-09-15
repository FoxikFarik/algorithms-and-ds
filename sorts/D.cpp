#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

int BubbleSort(vector<int>& A, int n){
    int swaps = 0;
    for(int i = 0; i < n-1; i++){
        bool sorted = true;
        for(int j = 0; j < n-i-1; j++){
            if(A[j] > A[j+1]){
                int temp = A[j+1];
                A[j+1] = A[j];
                A[j] = temp;
                sorted = false;
                swaps += 1;
            }
        }
        if(sorted) break;
    }
    return swaps;
}

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int& x : v) 
        cin >> x;
    cout << BubbleSort(v, n);
}
