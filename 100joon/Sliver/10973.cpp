#include <iostream>
#include <algorithm>

using namespace std;

int n;
int permute[10001];
int max_val;
int max_idx;
bool flag = 0;

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> permute[i];

    int mark;
    for (int i = n - 1; i > 0; i--)
    {
        if (permute[i - 1] > permute[i])
        {
            mark = i - 1;
            for (int j = mark + 1; j < n; j++)
            {
                if (permute[mark] > permute[j] && permute[j] > max_val)
                {
                    max_val = permute[j];
                    max_idx = j;
                }
            }
            swap(permute[mark], permute[max_idx]);
            sort(permute + mark + 1, permute + n, greater<>());
            flag = 1;
            break;
        }
    }

    if (flag)
    {
        for (int i = 0; i < n; i++)
            cout << permute[i] << ' ';
    }
    else
        cout << -1;

    return 0;
}