#include <iostream>
#include <vector>
using namespace std;

bool good(const vector<int>& v, int N, int K, int len){
    if(len == 0)
        return 1;

    int total_k = 0;
    for(int i = 0; i < N && total_k < K; i++)
        total_k += v[i] / len;

    return total_k >= K;
}

int bin_search(const vector<int>& v, int N, int K){
    int l = 0;
    int r = 100000000;
    while(r - l > 1){
        int m = (l + r) / 2;
        if(good(v, N, K, m))
            l = m;
        else
            r = m;
    }
    return l;
}

int main(){
    int N, K;
    cin >> N >> K;
    vector<int> v(N);
    for(int i = 0; i < N; i++)
        cin >> v[i];

    cout << bin_search(v, N, K) << endl;
    return 0;
}