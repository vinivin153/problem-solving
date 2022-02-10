#include <iostream>

using namespace std;

int n, m;
bool visited[9];

void seq(int idx, int cnt)
{
    if (cnt == m)
    {
        for (int i = 1; i <= n; i++)
            if (visited[i])
                cout << i << ' ';
        cout << '\n';
    }
    else
    {
        for (int i = idx; i <= n; i++)
        {
            if (!visited[i])
            {
                visited[i] = 1;
                seq(i, cnt + 1);
                visited[i] = 0;
            }
        }
    }
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;

    seq(1, 0);

    return 0;
}