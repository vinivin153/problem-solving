class Node {
  constructor(value, next) {
    this.value = value;
    this.next = next;
  }
}

class Queue {
  head;
  tail;

  isEmpty() {
    return !this.head;
  }

  push(value) {
    const node = new Node(value, null);
    if (!this.head) this.head = node;
    else this.tail.next = node;

    this.tail = node;
  }

  shift() {
    if (this.isEmpty()) return null;

    const res = this.head.value;
    this.head = this.head.next;
    return res;
  }
}

const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

const n = Number(input[0]);
const mat = input.slice(1).map((line) => line.split(''));

const door = [];
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (mat[i][j] === '#') door.push([i, j]);
  }
}
const [start, end] = [...door];

// 상 우 하 좌
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

function isCanMove(r, c) {
  return 0 <= r && r < n && 0 <= c && c < n && mat[r][c] !== '*';
}

function bfs() {
  let ans = Infinity;
  const queue = new Queue();
  const visited = Array.from({ length: n }, () =>
    Array.from({ length: n }, () => Array(4).fill(Infinity))
  );

  for (let i = 0; i < 4; i++) {
    queue.push([...start, i, 0]);
    visited[start[0]][start[1]][i] = 0;
  }

  while (!queue.isEmpty()) {
    const [x, y, d, cnt] = queue.shift();

    if (x === end[0] && y === end[1]) {
      ans = Math.min(ans, cnt);
    }

    if (cnt > visited[x][y][d]) continue;

    // 거울을 설치하는 경우
    if (mat[x][y] === '!') {
      const d1 = (d + 3) % 4;
      const d2 = (d + 1) % 4;
      for (let nd of [d1, d2]) {
        const nx = x + dx[nd];
        const ny = y + dy[nd];
        if (isCanMove(nx, ny) && visited[nx][ny][nd] > cnt + 1) {
          visited[nx][ny][nd] = cnt + 1;
          queue.push([nx, ny, nd, cnt + 1]);
        }
      }
    }

    // 설치하지 않는 경우
    const nx = x + dx[d];
    const ny = y + dy[d];
    if (isCanMove(nx, ny) && visited[nx][ny][d] > cnt) {
      visited[nx][ny][d] = cnt;
      queue.push([nx, ny, d, cnt]);
    }
  }

  return ans;
}
console.log(bfs());
