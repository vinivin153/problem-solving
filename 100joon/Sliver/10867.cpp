#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, num;
    cin >> n;

    set<int> nums;

    while (n--)
    {
        cin >> num;
        nums.insert(num);
    }

    for (auto iter = nums.begin(); iter != nums.end(); iter++)
        cout << *iter << ' ';

    return 0;
}