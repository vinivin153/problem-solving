#include <iostream>

using namespace std;

string n;
int m;
int button[10]{0};

int check(int num)
{
    if (num == 0)
        return 1;
    int len = 0;
    while (num)
    {
        if (button[num % 10])
            return 0;

        num /= 10;
        len += 1;
    }

    return len;
}

int main()
{
    iostream::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n;
    cin >> m;

    int nn = stoi(n);
    int min_val = abs(nn - 100);

    while (m--)
    {
        int tmp;
        cin >> tmp;
        button[tmp] = 1;
    }

    for (int i = 0; i <= 1000000; i++)
    {
        int cnt = check(i);

        if (cnt && !button[i % 10])
            min_val = min(min_val, cnt + abs(i - nn));
    }

    cout << min_val;

    return 0;
}