#include <iostream>
#include <algorithm>

using namespace std;

int n;
int permute[10001]{0};
bool flag = 0;
int min_val = 10001;
int min_idx;

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
        if (permute[i - 1] < permute[i])
        {
            mark = i - 1;
            for (int j = mark + 1; j < n; j++)
            {
                if (permute[j] > permute[mark] && permute[j] < min_val)
                {
                    min_val = permute[j];
                    min_idx = j;
                }
            }
            swap(permute[min_idx], permute[mark]);
            sort(permute + mark + 1, permute + n);
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