#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

auto cal(int a, int b)
{
    pair<int, int> ret;
    while (1)
    {
        int c = gcd(a, b);
        if (c == 1)
            break;
        else
        {
            a /= c;
            b /= c;
        }
    }
    ret.first = a;
    ret.second = b;

    return ret;
}

int main()
{
    iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;
    vector<int> rings(n);
    for (int i = 0; i < n; i++)
        cin >> rings[i];

    for (int i = 1; i < n; i++)
    {
        auto p = cal(rings[0], rings[i]);
        cout << p.first << "/" << p.second << "\n";
    }

    return 0;
}