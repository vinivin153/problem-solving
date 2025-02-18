const input = require("fs").readFileSync("input.txt", "utf-8").split("\n");

class Queue {
  constructor() {
    this.queue = {};
    this.front = 0;
    this.rear = 0;
  }

  push(element) {
    this.queue[this.front++] = element;
  }

  isEmpty() {
    return this.front === this.rear;
  }

  shift() {
    if (this.isEmpty()) {
      console.log("비어있음");
      return;
    }

    const element = this.queue[this.rear++];
    return element;
  }

  size() {
    return this.front - this.rear;
  }
}

const [n, m] = input[0].split(" ");
const mat = Array.from({ length: n }, (_, idx) =>
  input[idx + 1].split("").map(Number)
);
const visited = Array.from({ length: n }, () =>
  Array.from({ length: m }, () => Array(2).fill(0))
);

const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];
let ans = -1;
const queue = new Queue();
queue.push([0, 0, 0, 1]);
while (queue.size()) {
  const [x, y, z, cnt] = queue.shift();
  if (x === n - 1 && y === m - 1) {
    ans = cnt;
    break;
  }

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (0 <= nx && nx < n && 0 <= ny && ny < m) {
      // 이동 가능
      if (mat[nx][ny] === 0 && !visited[nx][ny][z]) {
        queue.push([nx, ny, z, cnt + 1]);
        visited[nx][ny][z] = 1;
      } else if (mat[nx][ny] === 1 && z === 0 && !visited[nx][ny][z + 1]) {
        queue.push([nx, ny, z + 1, cnt + 1]);
        visited[nx][ny][z + 1] = 1;
      }
    }
  }
}

console.log(ans);
