#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(string a, string b)
{
    return a + b > b + a;
}

string solution(vector<int> numbers)
{
    string answer = "";

    vector<string> v;

    for (int n : numbers)
    {
        v.push_back(to_string(n));
    }

    sort(v.begin(), v.end(), compare);

    for (string i : v)
        answer += i;

    if (answer[0] == '0')
        answer = '0';

    return answer;
}