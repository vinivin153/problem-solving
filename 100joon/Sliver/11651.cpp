#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.second == b.second)
        return a.first < b.first;
    return a.second < b.second;
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, x, y;
    cin >> n;

    vector<pair<int, int>> loc;
    while (n--)
    {
        cin >> x >> y;
        loc.push_back(pair<int, int>(x, y));
    }

    sort(loc.begin(), loc.end(), compare);

    for (auto &i : loc)
        cout << i.first << ' ' << i.second << '\n';

    return 0;
}