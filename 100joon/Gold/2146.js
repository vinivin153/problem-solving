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

  push(element) {
    const node = new Node(element, null);
    if (this.head) this.tail.next = node;
    else this.head = node;
    this.tail = node;
  }

  shift() {
    if (this.isEmpty()) return undefined;
    const result = this.head.value;
    this.head = this.head.next;

    return result;
  }
}

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const n = Number(input[0]);
const mat = input.slice(1).map((line) => line.split(' ').map(Number));
const visited = Array.from({ length: n }, () => Array(n).fill(false));
const group = [];

const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];

function isValidScope(r, c) {
  return 0 <= r && r < n && 0 <= c && c < n;
}

function bfs(r, c) {
  const side = [];
  const queue = new Queue();
  queue.push([r, c]);
  visited[r][c] = true;
  while (!queue.isEmpty()) {
    const [x, y] = queue.shift();

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (isValidScope(nx, ny) && !visited[nx][ny]) {
        if (mat[nx][ny] === 1) {
          queue.push([nx, ny]);
        } else {
          side.push([nx, ny]);
        }

        visited[nx][ny] = true;
      }
    }
  }
  side.sort((a, b) => {
    if (a[0] === b[0]) {
      return a[1] - b[1];
    }
    return a[0] - b[0];
  });
  return side;
}

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (!visited[i][j] && mat[i][j] === 1) {
      const result = bfs(i, j);
      group.push(result);
    }
  }
}

let ans = Infinity;
const countGroup = group.length;
for (let g1 = 0; g1 < countGroup - 1; g1++) {
  for (let g2 = g1 + 1; g2 < countGroup; g2++) {
    for (let [x1, y1] of group[g1]) {
      for (let [x2, y2] of group[g2]) {
        const dist = Math.abs(x2 - x1) + Math.abs(y2 - y1) + 1;
        if (dist < ans) {
          ans = dist;
        }
      }
    }
  }
}

console.log(ans);
