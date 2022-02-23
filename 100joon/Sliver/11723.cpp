#include <iostream>
#include <set>
#include <string>

using namespace std;

int m;
set<int> s;

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> m;

    string com;
    int x;

    while (m--)
    {
        cin >> com;
        if (com[1] == 'd')
        {
            cin >> x;
            s.insert(x);
        }
        else if (com[0] == 'r')
        {
            cin >> x;
            s.erase(x);
        }
        else if (com[0] == 'c')
        {
            cin >> x;
            if (s.find(x) == s.end())
                cout << 0 << '\n';
            else
                cout << 1 << '\n';
        }
        else if (com[0] == 't')
        {
            cin >> x;
            if (s.find(x) == s.end())
                s.insert(x);
            else
                s.erase(x);
        }
        else if (com[0] == 'a')
            s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
        else
            s = {};
    }

    return 0;
}