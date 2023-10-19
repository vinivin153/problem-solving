#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> citations)
{
    sort(citations.begin(), citations.end(), greater<int>());

    citations.insert(citations.begin(), 10001);

    int answer = citations.size() - 1;
    for (int i = 1; i < citations.size(); i++)
    {
        if (citations[i] < i)
        {
            answer = i - 1;
            break;
        }
    }

    return answer;
}