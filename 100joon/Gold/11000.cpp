#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.second == b.second)
        return a.first > b.first;
    else
        return a.second > b.second;
}

priority_queue<int> pq;
vector<pair<int, int>> v;

int main()
{
    iostream::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    while (n--)
    {
        int s, t;
        cin >> s >> t;
        v.push_back(pair<int, int>{s, t});
    }

    int cnt = 1;
    sort(v.begin(), v.end(), compare);

    pq.push(v[0].first);

    for (int i = 1; i < v.size(); i++)
    {
        int num = pq.top();
        if (v[i].second <= num)
            pq.pop();
        else
            cnt++;

        pq.push(v[i].first);
    }

    cout << cnt;
    return 0;
}