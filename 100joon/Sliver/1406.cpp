#include <iostream>
#include <string>
#include <list>

using namespace std;

int main()
{
    iostream::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    string s;
    list<char> a;

    cin >> s;
    for (auto i : s)
        a.push_back(i);

    auto loc = a.end();

    int m = 0;
    char ch;
    cin >> m;

    for (int i = 0; i < m; i++)
    {
        char input;
        cin >> input;

        if (input == 'L')
        {
            if (loc != a.begin())
                loc--;
        }
        else if (input == 'D')
        {
            if (loc != a.end())
                loc++;
        }
        else if (input == 'B')
        {
            if (loc != a.begin())
            {
                loc--;
                loc = a.erase(loc);
            }
        }
        else if (input == 'P')
        {
            cin >> ch;
            a.insert(loc, ch);
        }
    }
    for (char c : a)
        cout << c;

    return 0;
}