#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.first == b.first)
        return a.second < b.second;
    return a.first < b.first;
}

int main()
{
    iostream::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    int x, y;
    vector<pair<int, int>> pos;
    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        pos.push_back(pair(x, y));
    }

    sort(pos.begin(), pos.end(), compare);

    for (auto i : pos)
        cout << i.first << ' ' << i.second << '\n';

    return 0;
}