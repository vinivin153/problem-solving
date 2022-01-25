#include <iostream>
using namespace std;

unsigned long long combi(int a, int b)
{
    unsigned long long result1 = 1;
    unsigned long long result2 = 1;
    int k = b;
    int cnt = min(a, b - a);
    while (cnt > 0)
    {
        result1 *= k;
        cnt--;
        k--;
    }
    for (int i = 1; i <= min(a, b - a); i++)
        result2 *= i;

    return result1 / result2;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n, m;
        cin >> n >> m;
        cout << combi(n, m) << '\n';
    }

    return 0;
}