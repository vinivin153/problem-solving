#include <stdio.h>
#define MAX 2187

int map[MAX][MAX] = {
    0,
};

void star(int n, int r, int c);

int main()
{
    int n;
    scanf("%d", &n);

    star(n, 0, 0);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (map[i][j] == 1)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
}

void star(int n, int r, int c)
{
    if (n == 3)
    {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                map[i + r][j + c] = 1;
        map[r + 1][c + 1] = 0;
    }
    else
    {
        int k = n / 3;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (i == 1 && j == 1)
                    continue;
                else
                    star(k, r + k * i, c + k * j);
            }
        }
    }
}