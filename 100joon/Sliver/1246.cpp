#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> p;

    int temp;
    for (int i = 0; i < m; i++)
    {
        cin >> temp;
        p.push_back(temp);
    }
    sort(p.begin(), p.end());

    int max_profit = 0;
    int v = 0;
    for (int i = 0; i < m; i++)
    {
        if (max_profit < min(n, m - i) * p[i])
        {
            max_profit = min(n, m - i) * p[i];
            v = p[i];
        }
    }
    cout << v << " " << max_profit;

    return 0;
}