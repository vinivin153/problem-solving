#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t;
    cin >> t;

    while (t--)
    {
        string s;
        vector<bool> stack;
        cin >> s;
        bool flag = true;

        for (auto i : s)
        {
            if (i == '(')
                stack.push_back(1);
            else if (stack.empty())
            {
                flag = false;
                break;
            }
            else
                stack.pop_back();
        }
        if (!stack.empty())
            flag = false;

        cout << (flag ? "YES" : "NO") << '\n';
    }

    return 0;
}