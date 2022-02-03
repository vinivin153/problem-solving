// bst로 다시 풀어보기
#include <iostream>
#include <unordered_map>

using namespace std;

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, m, t;
    unordered_map<int, int> a;
    cin >> n;
    while (n--)
    {
        cin >> t;
        if (a[t])
            a[t]++;
        else
            a[t] = 1;
    }

    cin >> m;
    while (m--)
    {
        cin >> t;
        cout << a[t] << ' ';
    }

    return 0;
}