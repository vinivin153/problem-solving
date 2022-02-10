#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<int> s;

void seq(int cnt)
{
    if (s.size() == m)
    {
        for (auto &i : s)
            cout << i << ' ';
        cout << '\n';
    }
    else
    {
        for (int i = 1; i <= n; i++)
        {
            s.push_back(i);
            seq(cnt + 1);
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

    seq(0);

    return 0;
}