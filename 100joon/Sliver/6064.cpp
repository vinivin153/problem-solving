#include <iostream>

using namespace std;

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 0;
    cin >> t;
    int m, n, x, y;
    int year, big, small, cmp, ss;

    while (t--)
    {
        bool visited[40001]{false};
        cin >> m >> n >> x >> y;
        if (m > n)
        {
            big = m;
            small = n;
            year = x;
            cmp = y;
            ss = x % small;
        }
        else
        {
            big = n;
            small = m;
            cmp = x;
            year = y;
            ss = y % small;
        }
        if (ss == 0)
            ss = small;
        visited[ss] = true;
        while (ss != cmp)
        {
            ss += big;
            ss %= small;
            if (ss == 0)
                ss = small;
            if (visited[ss])
            {
                year = -1;
                break;
            }
            else
                visited[ss] = true;

            year += big;
        }

        cout << year << '\n';
    }
}
