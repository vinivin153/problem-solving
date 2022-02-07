#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int max_len = 1;
vector<vector<char>> board(n);

void check_len(int a, int b)
{
    int tmp = 1;
    for (int i = 0; i < n - 1; i++)
    {
        if (max_len >= n - i && tmp == 1)
            break;

        if (board[a][i] == board[a][i + 1])
            tmp++;
        else
        {
            max_len = max(tmp, max_len);
            tmp = 1;
        }
    }
    max_len = max(tmp, max_len);

    tmp = 1;
    for (int i = 0; i < n - 1; i++)
    {
        if (max_len >= n - i && tmp == 1)
            break;

        if (board[i][b] == board[i + 1][b])
            tmp++;
        else
        {
            max_len = max(tmp, max_len);
            tmp = 1;
        }
    }
    max_len = max(tmp, max_len);
}

void swap_candy(int a, int b)
{
    int dx[4]{-1, 1, 0, 0};
    int dy[4]{0, 0, -1, 1};

    for (int i = 0; i < 4; i++)
    {
        int nx = a + dx[i];
        int ny = b + dy[i];
        if (0 <= nx && nx < n && 0 <= ny && ny < n)
        {
            swap(board[a][b], board[nx][ny]);
            check_len(a, b);
            swap(board[a][b], board[nx][ny]);
        }
    }
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;

    board.assign(n, vector<char>(n, 0));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> board[i][j];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            check_len(i, j);
            swap_candy(i, j);
        }
    }

    cout << max_len;

    return 0;
}