#include <iostream>
using namespace std;

bool good(long long w, long long h, long long n, long long s){
    long long rows = s / h;
    long long cols = s / w;
    return rows * cols >= n;
}

long long bin_search(long long w, long long h, long long n){
    long long l = 1;
    long long r = max(w, h) * n;
    while(l < r){
        long long m = (l + r) / 2;
        if(good(w, h, n, m))
            r = m;
        else
            l = m+1;
    }
    return l;
}

int main(){
    long long w, h, n;
    cin >> w >> h >> n;

    cout << bin_search(w, h, n);
    return 0;
}