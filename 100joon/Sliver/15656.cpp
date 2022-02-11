#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
vector<int> arr;
vector<int> s;

void seq(int cnt)
{
    if (cnt == m)
    {
        for (auto &i : s)
            cout << i << ' ';
        cout << '\n';
        return;
    }

    for (int i = 0; i < n; i++)
    {
        s.push_back(arr[i]);
        seq(cnt + 1);
        s.pop_back();
    }
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;

    int tmp;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        arr.push_back(tmp);
    }

    sort(arr.begin(), arr.end());
    seq(0);
    return 0;
}