#include <iostream>
#include <vector>

using namespace std;

int main()
{
    iostream::sync_with_stdio(false);
    cin.tie(nullptr), cout.tie(nullptr);

    int a, b;
    cin >> a >> b;

    vector<int> seq;
    int i = 1;
    while (seq.size() < 1000)
    {
        for (int j = 0; j < i; j++)
            seq.push_back(i);
        i++;
    }

    int result = 0;
    for (int j = a - 1; j <= b - 1; j++)
        result += seq[j];

    cout << result;

    return 0;
}