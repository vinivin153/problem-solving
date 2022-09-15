// 완전탐색 - 피로도
function solution(k, dungeons) {
    let maxCnt = 0;
    let visited = new Array(10).fill(false);

    function dfs(cnt, left) {
        for (let i = 0; i < dungeons.length; i++) {
            if (visited[i] === false && left >= dungeons[i][0]) {
                visited[i] = true;
                dfs(cnt + 1, left - dungeons[i][1])
                visited[i] = false;
            }
        }
        maxCnt = Math.max(maxCnt, cnt);
    }
    dfs(0, k);
    return maxCnt;
}