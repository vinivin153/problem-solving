// dfs로 풀어보기
#include <iostream>
#include <vector>

using namespace std;

int n, m;
int max_val = 0;
vector<vector<int>> mat;

void shape1()
{
    int sum1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m - 3; j++)
        {
            sum1 = 0;
            for (int k = 0; k < 4; k++)
            {
                sum1 += mat[i][j + k];
                max_val = max(max_val, sum1);
            }
        }
    }

    for (int i = 0; i < n - 3; i++)
    {
        for (int j = 0; j < m; j++)
        {
            sum1 = 0;
            for (int k = 0; k < 4; k++)
            {
                sum1 += mat[i + k][j];
                max_val = max(max_val, sum1);
            }
        }
    }
}

void shape2()
{
    int sum1;
    for (int i = 0; i < n - 1; i++)
    {
        sum1 = 0;
        for (int j = 0; j < m - 1; j++)
        {
            sum1 = mat[i][j] + mat[i][j + 1] + mat[i + 1][j] + mat[i + 1][j + 1];
            max_val = max(max_val, sum1);
        }
    }
}

void shape3()
{
    int sum1;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < m - 2; j++)
        {
            sum1 = mat[i][j] + mat[i][j + 1] + mat[i][j + 2] + mat[i + 1][j];
            max_val = max(max_val, sum1);
            sum1 = mat[i][j] + mat[i][j + 1] + mat[i][j + 2] + mat[i + 1][j + 2];
            max_val = max(max_val, sum1);
            sum1 = mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 1][j + 2] + mat[i][j];
            max_val = max(max_val, sum1);
            sum1 = mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 1][j + 2] + mat[i][j + 2];
            max_val = max(max_val, sum1);
        }
    }

    for (int i = 0; i < n - 2; i++)
    {
        for (int j = 0; j < m - 1; j++)
        {
            sum1 = mat[i][j] + mat[i + 1][j] + mat[i + 2][j] + mat[i][j + 1];
            max_val = max(max_val, sum1);
            sum1 = mat[i][j] + mat[i + 1][j] + mat[i + 2][j] + mat[i + 2][j + 1];
            max_val = max(max_val, sum1);
            sum1 = mat[i][j + 1] + mat[i + 1][j + 1] + mat[i + 2][j + 1] + mat[i][j];
            max_val = max(max_val, sum1);
            sum1 = mat[i][j + 1] + mat[i + 1][j + 1] + mat[i + 2][j + 1] + mat[i + 2][j];
            max_val = max(max_val, sum1);
        }
    }
}

void shape4()
{
    int sum1;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < m - 2; j++)
        {
            sum1 = mat[i][j] + mat[i][j + 1] + mat[i + 1][j + 1] + mat[i + 1][j + 2];
            max_val = max(max_val, sum1);
            sum1 = mat[i + 1][j] + mat[i + 1][j + 1] + mat[i][j + 1] + mat[i][j + 2];
            max_val = max(max_val, sum1);
        }
    }

    for (int i = 0; i < n - 2; i++)
    {
        for (int j = 0; j < m - 1; j++)
        {
            sum1 = mat[i][j] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 2][j + 1];
            max_val = max(max_val, sum1);
            sum1 = mat[i][j + 1] + mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 2][j];
            max_val = max(max_val, sum1);
        }
    }
}

void shape5()
{
    int sum1;
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < m - 2; j++)
        {
            sum1 = mat[i][j] + mat[i][j + 1] + mat[i][j + 2] + mat[i + 1][j + 1];
            max_val = max(max_val, sum1);
            sum1 = mat[i + 1][j] + mat[i + 1][j + 1] + mat[i + 1][j + 2] + mat[i][j + 1];
            max_val = max(max_val, sum1);
        }
    }

    for (int i = 0; i < n - 2; i++)
    {
        for (int j = 0; j < m - 1; j++)
        {
            sum1 = mat[i][j] + mat[i + 1][j] + mat[i + 2][j] + mat[i + 1][j + 1];
            max_val = max(max_val, sum1);
            sum1 = mat[i][j + 1] + mat[i + 1][j + 1] + mat[i + 2][j + 1] + mat[i + 1][j];
            max_val = max(max_val, sum1);
        }
    }
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    mat.assign(n, vector<int>(m));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> mat[i][j];

    shape1();
    shape2();
    shape3();
    shape4();
    shape5();

    cout << max_val;
}