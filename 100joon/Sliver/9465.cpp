#include <iostream>
#include <vector>

using namespace std;

int main()
{
    iostream::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t, n;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> n;
        vector<vector<int>> sticker(2, vector<int>(n, 0));
        for (int j = 0; j < n; j++)
            cin >> sticker[0][j];

        for (int j = 0; j < n; j++)
            cin >> sticker[1][j];

        vector<vector<int>> dp(2, vector<int>(n + 1, 0));
        dp[0][0] = 0;
        dp[1][0] = 0;
        dp[0][1] = sticker[0][0];
        dp[1][1] = sticker[1][0];

        for (int j = 2; j < n + 1; j++)
        {
            dp[0][j] = sticker[0][j - 1] + max(dp[1][j - 1], dp[1][j - 2]);
            dp[1][j] = sticker[1][j - 1] + max(dp[0][j - 1], dp[0][j - 2]);
        }

        cout << max(dp[0].back(), dp[1].back()) << '\n';
    }
}