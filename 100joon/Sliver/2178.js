const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const mat = Array.from({ length: n }, (_, idx) =>
  input[idx + 1].split('').map(Number)
);
const visited = Array.from({ length: n }, () => Array(m).fill(false));

const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];

function bfs() {
  const stack = [];
  stack.push([0, 0, 1]);
  visited[0][0] = true;
  while (stack) {
    const [x, y, cnt] = stack.shift();

    if (x === n - 1 && y === m - 1) {
      console.log(cnt);
      return;
    }

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (!visited[nx][ny] && mat[nx][ny] === 1) {
          stack.push([nx, ny, cnt + 1]);
          visited[nx][ny] = true;
        }
      }
    }
  }
}

bfs();
