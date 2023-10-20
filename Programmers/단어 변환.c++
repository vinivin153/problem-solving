#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

using namespace std;

bool compare(string a, string b) {
    int cnt = 0;
    for (int i; i < a.length(); i++) {
        if (a[i] != b[i]) {
            cnt += 1;
        }

        if (cnt >= 2) {
            break;
        }
    }

    if (cnt == 0 || cnt >= 2)
        return false;

    return true;
}

int solution(string begin, string target, vector<string> words) {
    map<string, int> visited;
    for (auto word : words) {
        visited[word] = 0;
    }

    queue<string> q;
    q.push(begin);
    while (!q.empty()) {
        string s = q.front();
        q.pop();

        if (target == s) {
            return visited[target];
        }

        for (auto word : words) {
            if (!visited[word] && compare(s, word)) {
                q.push(word);
                visited[word] = visited[s] + 1;
            }
        }
    }

    return 0;
}