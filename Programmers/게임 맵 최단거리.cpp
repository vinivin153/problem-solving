#include<vector>
#include<queue>
using namespace std;

int solution(vector<vector<int> > maps)
{    
    int row = maps.size();
    int col = maps[0].size();
    
    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    
    int dx[] = {0, 0, -1, 1};
    int dy[] = {1, -1, 0, 0};
    
    maps[0][0] = 1;
    
    while (!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        if (x == row - 1 && y == col - 1){
            return maps[x][y];
        }
        
        for(int i = 0 ; i < 4 ; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if((0 <= nx && nx < row && 0 <= ny && ny < col)) {
                if(maps[nx][ny] == 1) {
                    q.push(make_pair(nx, ny));
                    maps[nx][ny] = maps[x][y] + 1;
                }
            }
        }
    }
    
    return -1;
}