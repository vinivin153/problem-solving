#include <iostream>

using namespace std;

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    long long int sum1 = 0;
    for (int i = 1; i <= n; i++)
        sum1 += (n / i) * i;

    cout << sum1;

    return 0;
}