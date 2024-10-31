const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

class Queue {
  constructor() {
    this.queue = {};
    this.front = 0;
    this.rear = 0;
  }

  append(element) {
    this.queue[this.rear++] = element;
  }

  popleft() {
    if (this.isEmpty()) {
      return "큐가 비었습니다";
    }

    const item = this.queue[this.front];
    delete this.queue[this.front];
    this.front++;

    return item;
  }

  size() {
    return this.rear - this.front;
  }

  isEmpty() {
    return this.rear === this.front;
  }

  peek() {
    return this.queue[rear];
  }
}

let myPos = [0, 0];
let exit = [];
const ghost = [];
const lines = [];

rl.on("line", (line) => {
  lines.push(line);
}).on("close", () => {
  const [n, m] = lines[0].split(" ").map(Number);
  const arr = lines.slice(1, n + 1).map((line) => line.split(""));
  let ans = "No";

  findPos(arr, n, m);
  let dist = Math.pow(10, 9);
  for (let g of ghost) {
    const [x1, y1] = g;
    const cDist = calcDist(x1, y1);
    if (cDist < dist) {
      dist = cDist;
    }
  }

  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];

  const queue = new Queue();
  queue.append([...myPos, 0]);
  visited = Array.from(Array(n), () => Array(m).fill(false));
  visited[myPos[0]][myPos[1]];
  while (!queue.isEmpty()) {
    const [x, y, cnt] = queue.popleft();
    if (arr[x][y] === "D") {
      ans = "Yes";
      break;
    }

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if ((!visited[nx][ny] && arr[nx][ny] === ".") || arr[nx][ny] === "D") {
          if (dist > cnt + 1) {
            queue.append([nx, ny, cnt + 1]);
            visited[nx][ny] = true;
          }
        }
      }
    }
  }

  console.log(ans);
  process.exit(0);
});

const findPos = (arr, n, m) => {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (arr[i][j] === "N") {
        myPos = [i, j];
      } else if (arr[i][j] === "D") {
        exit = [i, j];
      } else if (arr[i][j] === "G") {
        ghost.push([i, j]);
      }
    }
  }
};

const calcDist = (x1, y1) => {
  const [x2, y2] = exit;
  return Math.abs(x1 - x2) + Math.abs(y1 - y2);
};
