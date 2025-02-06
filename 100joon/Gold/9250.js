const input = require("fs")
  .readFileSync("input.txt", "utf-8")
  .trim()
  .split("\n");

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
    return this.front === this.rear;
  }

  popleft() {
    if (this.isEmpty()) {
      console.log("empty");
      return;
    }

    const temp = this.queue[this.front];
    delete this.queue[this.front++];
    return temp;
  }

  size() {
    return this.rear - this.front;
  }

  peak() {
    return this.queue[rear];
  }
}

function calcDist(x1, y1, x2, y2) {
  return Math.abs(x1 - x2) + Math.abs(y1 - y2);
}

const t = Number(input[0]);
let idx = 1;
for (let _ = 0; _ < t; _++) {
  const n = input[idx++];
  const [startX, startY] = input[idx++].split(" ").map(Number);
  const conven = {};
  for (let j = 0; j < n; j++) {
    const [x, y] = input[idx++].split(" ").map(Number);
    conven[j] = [x, y];
  }

  const [endX, endY] = input[idx++].split(" ").map(Number);

  let ans = "sad";
  const queue = new Queue();
  queue.append([startX, startY]);
  while (!queue.isEmpty()) {
    const [x, y] = queue.popleft();

    if (calcDist(x, y, endX, endY) <= 1000) {
      console.log(x, y);
      ans = "happy";
      break;
    }

    for (let j in { ...conven }) {
      const [nx, ny] = conven[j];
      if (calcDist(x, y, nx, ny) <= 1000) {
        delete conven[j];
        queue.append([nx, ny]);
      }
    }
  }
  console.log(ans);
}
