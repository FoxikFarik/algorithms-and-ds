#include <iostream>
#include <vector>
using namespace std;

bool good(const vector<int>& v, int N, int K, int dist){
    if(dist == 0 || K == 1)
        return 1;
    
    int placed = 1;
    int last_place = v[0];
    for(int i = 1; i < N && placed < K; i++){
        if(v[i] - last_place >= dist){
            last_place = v[i];
            placed++;
        }
    }

    return placed >= K;
}

int bin_search(const vector<int>& v, int N, int K){
    int l = 0;
    int r = v[N-1];
    while(r - l > 1){
        int m = (l + r) / 2;
        if(good(v, N, K, m))
            l = m;
        else
            r = m;
    }
    return l;
}

int main()
{
    int N, K;
    cin >> N >> K;
    vector<int> v(N);
    for(int i = 0; i < N; i++)
        cin >> v[i];

    cout << bin_search(v, N, K);
    return 0;
}