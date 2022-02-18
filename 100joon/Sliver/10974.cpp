#include <iostream>
#include <vector>

using namespace std;

int n;
bool visited[10];
vector<int> arr;

void backtracking(int cnt)
{
    if (cnt == n)
    {
        for (auto &i : arr)
            cout << i << ' ';
        cout << '\n';
        return;
    }

    for (int i = 1; i <= n; i++)
    {
        if (!visited[i])
        {
            visited[i] = 1;
            arr.push_back(i);
            backtracking(cnt + 1);
            arr.pop_back();
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

    backtracking(0);
    return 0;
}