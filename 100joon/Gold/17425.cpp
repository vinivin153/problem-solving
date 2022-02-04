#include <iostream>

using namespace std;

int t, num;
long long memo[1000001]{0};

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> t;

    for (int i = 1; i < 1000001; i++)
        for (int j = 1; j <= 1000000 / i; j++)
            memo[i * j] += i;

    for (int i = 2; i < 1000001; i++)
        memo[i] = memo[i - 1] + memo[i];

    while (t--)
    {
        cin >> num;
        cout << memo[num] << '\n';
    }

    return 0;
}