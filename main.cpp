#include <bits/stdc++.h>

using namespace std;
int l,r;
const long long MOD = 1e9 + 7;
long long a[2000006], dem;

int fun(int x){
    if (x < 2) return 1;
    return (x+1)*fun(x-1);
}

int main()
{
    int a = 0;
    if(a) cout << 0;
    else cout << 1;
}
