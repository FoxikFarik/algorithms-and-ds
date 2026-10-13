#include <iostream>
using namespace std;

bool good(long long t, long long x, long long y, long long N){
    return t / x + t / y >= N;
}

long long bin_search(long long x, long long y, long long N){
    if(N == 1)
        return min(x, y);

    long long l = 0;
    long long r = N * min(x, y);
    while(l < r){
        long long m = (l + r) / 2;
        if(good(m, x, y, N-1))
            r = m;
        else
            l = m + 1;
    }
    return l + min(x, y);
}

int main()
{
    long long N, x, y;
    cin >> N >> x >> y;
    cout << bin_search(x, y, N) << endl;

    return 0;
}