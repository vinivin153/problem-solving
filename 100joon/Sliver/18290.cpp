#include <iostream>
#include <vector>

using namespace std;

int n, m, k;
int mat[11][11];
int ans = -1000001, sum1 = 0;
bool visited[11][11]{0};

void backtracking(int x, int y, int cnt)
{
    if (cnt == k)
    {
        ans = max(ans, sum1);
        return;
    }

    for (int i = x; i <= n; i++)
    {
        if (i > x)
            y = 1;
        for (int j = y; j <= m; j++)
        {
            if (!visited[i][j] && !visited[i - 1][j] && !visited[i][j - 1])
            {
                visited[i][j] = 1;
                sum1 += mat[i][j];
                backtracking(i, j, cnt + 1);
                visited[i][j] = 0;
                sum1 -= mat[i][j];
            }
        }
    }
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m >> k;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> mat[i][j];

    backtracking(1, 1, 0);
    cout << ans;

    return 0;
}