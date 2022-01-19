#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<string> name(n);
    vector<int> val(n);

    int min_val = 30000000, max_val = 0;
    int min_idx = 0, max_idx = 0;
    for (int i = 0; i < n; i++)
    {
        int d, m, y;
        cin >> name[i] >> d >> m >> y;
        val[i] = y * 10000 + m * 100 + d;
        if (max_val < val[i])
        {
            max_val = val[i];
            max_idx = i;
        }

        if (min_val > val[i])
        {
            min_val = val[i];
            min_idx = i;
        }
    }

    cout << name[max_idx] << endl;
    cout << name[min_idx] << endl;
}