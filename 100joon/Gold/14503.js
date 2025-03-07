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
const [n, m] = input[0].split(' ').map(Number);
let [robotX, robotY, d] = input[1].split(' ').map(Number);
const mat = input.slice(2).map((line) => line.split(' ').map(Number));
const CLEAN = 2;
const NOT_CLEAN = 0;
const WALL = 1;
let ans = 0;

// 북 동 남 서
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

function runRobot() {
  const queue = new Queue();
  queue.push([robotX, robotY, d]);
  while (!queue.isEmpty()) {
    const [x, y, direction] = queue.shift();

    // 1. 현재 칸 청소
    if (mat[x][y] === NOT_CLEAN) {
      mat[x][y] = CLEAN;
      ans++;
    }

    let isClean = true;
    for (let i = 3; i >= 0; i--) {
      const newDirection = (direction + i) % 4;
      const nx = x + dx[newDirection];
      const ny = y + dy[newDirection];
      // 3. 청소되지 않은 빈 칸이 있는 경우
      if (mat[nx][ny] === NOT_CLEAN) {
        queue.push([nx, ny, newDirection]);
        isClean = false;
        break;
      }
    }

    if (!isClean) continue;

    // 2. 청소되지않은 빈 칸이 없는 경우
    const nx = x - dx[direction];
    const ny = y - dy[direction];
    if (mat[nx][ny] !== WALL) {
      queue.push([nx, ny, direction]);
    } else break;
  }
}

runRobot();
console.log(ans);
