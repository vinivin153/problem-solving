#include <iostream>
#include <string>

using namespace std;

int k;
char arr[10];
bool visited[10]{0};
string s = "";
string max_val = "0";
string min_val = "9999999999";

void solve(int idx, int cnt)
{
    if (cnt == k)
    {
        max_val = max(max_val, s);
        min_val = min(min_val, s);
        return;
    }

    if (arr[cnt] == '<')
    {
        for (int i = idx; i <= 9; i++)
        {
            if (!visited[i])
            {
                visited[i] = 1;
                s.append(to_string(i));
                solve(i, cnt + 1);
                visited[i] = 0;
                s.pop_back();
            }
        }
    }
    else
    {
        for (int i = idx; i >= 0; i--)
        {
            if (!visited[i])
            {
                visited[i] = 1;
                s.append(to_string(i));
                solve(i, cnt + 1);
                visited[i] = 0;
                s.pop_back();
            }
        }
    }
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> k;
    for (int i = 0; i < k; i++)
        cin >> arr[i];

    for (int i = 0; i <= 9; i++)
    {
        visited[i] = 1;
        s = to_string(i);
        solve(i, 0);
        visited[i] = 0;
    }

    cout << max_val << '\n'
         << min_val;
    return 0;
}