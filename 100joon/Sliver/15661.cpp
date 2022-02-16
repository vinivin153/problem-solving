#include <iostream>

using namespace std;

int n;
int mat[20][20];
int start_val, link_val;
bool visited[20]{0};
int ans = 100000;

void solve(int cnt, int a, int idx)
{
    if (cnt == a)
    {
        start_val = 0;
        link_val = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (visited[i] && visited[j])
                    start_val += mat[i][j];
                else if (!visited[i] && !visited[j])
                    link_val += mat[i][j];
            }
        }

        ans = min(ans, abs(start_val - link_val));
        return;
    }

    for (int i = idx + 1; i < n; i++)
    {
        if (!visited[i])
        {
            visited[i] = 1;
            solve(cnt + 1, a, i);
            visited[i] = 0;
        }
    }
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> mat[i][j];

    for (int i = 1; i <= n / 2; i++)
    {
        if (ans == 0)
            break;
        solve(0, i, -1);
    }

    cout << ans;

    return 0;
}