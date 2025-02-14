const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");

class Queue {
  constructor() {
    this.queue = {};
    this.front = 0;
    this.rear = 0;
  }

  append(element) {
    this.queue[this.rear++] = element;
  }

  isEmpty() {
    return this.rear === this.front;
  }

  shift() {
    if (this.isEmpty()) {
      console.log("비어있음!");
      return;
    }

    return this.queue[this.front++];
  }

  size() {
    return this.rear - this.front;
  }
}

const k = Number(input[0]);
const [m, n] = input[1].split(" ").map(Number);
const mat = input.slice(2).map((line) => line.split(" ").map(Number));
const visited = Array.from({ length: n }, () =>
  Array.from({ length: m }, () => Array(k + 1).fill(0))
);

// 일반 이동
const dx1 = [0, 0, -1, 1];
const dy1 = [1, -1, 0, 0];

// 말의 움직임 8개
const dx2 = [-2, -2, -1, -1, 1, 1, 2, 2];
const dy2 = [-1, 1, -2, 2, -2, 2, -1, 1];

let ans = Infinity;

const queue = new Queue();
queue.append([0, 0, 0]);
while (queue.size()) {
  const [x, y, z] = queue.shift();

  if (x === n - 1 && y === m - 1) {
    ans = visited[x][y][z];
    break;
  }

  for (let i = 0; i < 4; i++) {
    const nx = x + dx1[i];
    const ny = y + dy1[i];
    if (!(nx < 0 || nx >= n || ny < 0 || ny >= m)) {
      if (mat[nx][ny] === 0 && !visited[nx][ny][z]) {
        visited[nx][ny][z] = visited[x][y][z] + 1;
        queue.append([nx, ny, z]);
      }
    }
  }

  if (z === k) continue;

  for (let i = 0; i < 8; i++) {
    const nx = x + dx2[i];
    const ny = y + dy2[i];
    if (!(nx < 0 || nx >= n || ny < 0 || ny >= m)) {
      if (mat[nx][ny] === 0 && !visited[nx][ny][z + 1]) {
        visited[nx][ny][z + 1] = visited[x][y][z] + 1;
        queue.append([nx, ny, z + 1]);
      }
    }
  }
}

if (ans === Infinity) {
  console.log(-1);
} else {
  console.log(ans);
}
