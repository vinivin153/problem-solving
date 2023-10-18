#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <tuple>

using namespace std;

int solution(vector<int> numbers, int target)
{
    int answer = 0;
    int num_len = numbers.size();

    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    while (!q.empty())
    {
        int sum = q.front().first;
        int idx = q.front().second;

        cout << sum << "" << idx;

        q.pop();

        if (sum == target && idx == num_len)
        {
            answer += 1;
            continue;
        }

        if (idx < num_len)
        {
            q.push(make_pair(sum + numbers[idx], idx + 1));
            q.push(make_pair(sum - numbers[idx], idx + 1));
        }
    }

    return answer;
}