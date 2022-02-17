#include <iostream>
#include <vector>

using namespace std;

int n;
char sign[11][11];
int s[11][11];
vector<int> ans;

pair<int, int> check(int a)
{
    pair<int, int> p;
    p.first = 0;
    p.second = 0;
    if (sign[a][a] == '+')
    {
        p.first = 1;
        p.second = 10;
    }
    else if (sign[a][a] == '-')
    {
        p.first = -10;
        p.second = -1;
    }
    return p;
}

void solve(int cnt)
{
    if (cnt == n)
    {
        for (auto &i : ans)
            cout << i << ' ';
        exit(0);
    }

    pair<int, int> tmp;
    tmp = check(cnt + 1);
    int s1 = tmp.first;
    int e1 = tmp.second;
    for (int i = s1; i <= e1; i++)
    {
        bool flag = 1;
        for (int j = 1; j <= cnt; j++)
        {
            char t = '0';
            s[j][cnt + 1] = i + s[j][cnt];
            if (s[j][cnt + 1] > 0)
                t = '+';
            else if (s[j][cnt + 1] < 0)
                t = '-';

            if (t != sign[j][cnt + 1])
            {
                flag = 0;
                break;
            }
        }
        if (flag)
        {
            s[cnt + 1][cnt + 1] = i;
            ans.push_back(i);
            solve(cnt + 1);
            ans.pop_back();
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
        for (int j = i; j <= n; j++)
            cin >> sign[i][j];

    pair<int, int> tmp;
    tmp = check(1);
    for (int i = tmp.first; i <= tmp.second; i++)
    {
        s[1][1] = i;
        ans.push_back(i);
        solve(1);
        ans.pop_back();
    }

    return 0;
}