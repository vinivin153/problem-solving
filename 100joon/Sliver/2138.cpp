// 다음에 더 최적화 시켜서 풀어보기 384ms...
#include <iostream>
#include <string>

using namespace std;

string ori, ans;
int n;

string push_switch(string s, int j)
{
    if (j + 1 < n)
        if (s[j + 1] == '0')
            s[j + 1] = '1';
        else
            s[j + 1] = '0';

    if (s[j] == '0')
        s[j] = '1';
    else
        s[j] = '0';

    if (s[j - 1] == '0')
        s[j - 1] = '1';
    else
        s[j - 1] = '0';

    return s;
}

int main()
{
    iostream::sync_with_stdio(false);
    cout.tie(nullptr);
    cin.tie(nullptr);

    cin >> n >> ori >> ans;

    string ori2 = ori;

    int cnt = 0;
    // 가장 앞에 스위치를 누르지 않았을 경우
    for (int i = 1; i < n; i++)
    {
        if (ori[i - 1] != ans[i - 1])
        {
            ori = push_switch(ori, i);
            cnt++;
        }

        if (ori == ans)
        {
            cout << cnt;
            return 0;
        }
    }

    //가장 앞 스위치를 누를경우
    cnt = 1;
    if (ori2[0] == '0')
        ori2[0] = '1';
    else
        ori2[0] = '0';

    if (ori2[1] == '0')
        ori2[1] = '1';
    else
        ori2[1] = '0';

    for (int i = 1; i < n; i++)
    {
        if (ori2[i - 1] != ans[i - 1])
        {
            ori2 = push_switch(ori2, i);
            cnt++;
        }

        if (ori2 == ans)
        {
            cout << cnt;
            return 0;
        }
    }

    cout << -1;

    return 0;
}