// DFS,BFS 게임 맵 최단거리
function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;

    dx = [0, 0, 1, -1];
    dy = [1, -1, 0, 0];
    function bfs() {
        let queue = [];
        queue.push([0, 0, 1]);
        maps[0][0] = -1;
        while (queue.length) {
            let [x, y, cnt] = queue.shift();
            if (x === n - 1 && y === m - 1) {
                return cnt;
            }
            for (let i = 0; i < 4; i++) {
                let nx = x + dx[i];
                let ny = y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (maps[nx][ny] === 1) {
                        queue.push([nx, ny, cnt + 1]);
                        maps[nx][ny] = -1;
                    }
                }
            }
        }
        return -1;
    }

    return bfs();
}