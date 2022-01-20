#include <stdio.h>
#include <string.h>

int main()
{
    int n, m;
    scanf("%d", &n);
    int nums[2001];
    bool palindrom[2001][2001]{false};
    // memset(palindrom, 0, sizeof(palindrom));

    for (int i = 1; i <= n; i++)
        scanf("%d", &nums[i]);

    for (int i = 1; i <= n; i++)
        palindrom[i][i] = true;

    for (int i = n - 1; i >= 1; i--)
        if (nums[i] == nums[i + 1])
            palindrom[i][i + 1] = true;

    for (int i = n - 2; i >= 1; i--)
        for (int j = i + 2; j <= n; j++)
            if (nums[i] == nums[j] && palindrom[i + 1][j - 1] == true)
                palindrom[i][j] = true;

    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        int s, e;
        scanf("%d %d", &s, &e);
        printf("%d\n", palindrom[s][e]);
    }

    return 0;
}
