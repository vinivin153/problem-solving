#include <iostream>

using namespace std;

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int e, s, m;
    cin >> e >> s >> m;

    int year = s;
    int ee, mm;
    ee = s % 15;
    mm = s % 19;
    if (ee == 0)
        ee = 15;
    if (mm == 0)
        mm = 19;
    while (ee != e or mm != m)
    {
        ee += 28;
        mm += 28;
        ee = ee % 15;
        mm = mm % 19;
        year += 28;
        if (ee == 0)
            ee = 15;
        if (mm == 0)
            mm = 19;
    }

    cout << year;

    return 0;
}