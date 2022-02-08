#include <iostream>
#include <string>

using namespace std;

int main()
{
    iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    int m = 9, cnt = 1, res = 0;
    while (1)
    {
        if (n - m >= 0)
        {
            n -= m;
            res += (cnt * m);
            cnt++;
        }
        else
        {
            res += (n * cnt);
            break;
        }
        m *= 10;
    }

    cout << res;

    return 0;
}