#include <iostream>

using namespace std;

int n;
int mat[11][11];
int min_val = 10000001;
bool visited[11]{0};
int start;

void solve(int cnt, int current, int val)
{
    if (cnt == n && mat[current][start])
    {
        val += mat[current][start];
        if (val < min_val)
            min_val = val;
        return;
    }

    if (val < min_val)
    {
        for (int i = 1; i <= n; i++)
        {
            if (!visited[i] && mat[current][i])
            {
                visited[i] = 1;
                solve(cnt + 1, i, val + mat[current][i]);
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

    cin >> n;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            cin >> mat[i][j];

    for (int i = 1; i <= n; i++)
    {
        start = i;
        visited[i] = 1;
        solve(1, i, 0);
        visited[i] = 0;
    }
    cout << min_val;

    return 0;
}