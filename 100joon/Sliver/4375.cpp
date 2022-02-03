#include <iostream>

using namespace std;
int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    while (cin >> n)
    {
        int cnt = 1;
        int val = 1;
        while (val % n)
        {
            val = (val % n) * 10 + 1;
            cnt++;
        }
        cout << cnt << '\n';
    }

    return 0;
}