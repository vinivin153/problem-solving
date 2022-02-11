#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<int> s;
bool visited[9];

void seq(int cnt, int idx)
{
    if (s.size() == m)
    {
        for (auto &i : s)
            cout << i << ' ';
        cout << '\n';
    }
    else
    {
        for (int i = idx; i <= n; i++)
        {
            s.push_back(i);
            seq(cnt + 1, i);
            s.pop_back();
        }
    }
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;

    seq(0, 1);

    return 0;
}