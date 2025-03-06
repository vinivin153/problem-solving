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

const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];
const result = [];
let idx = 0;
const t = Number(input[idx++]);
for (let tc = 0; tc < t; tc++) {
  const [m, n] = input[idx++].split(' ').map(Number);
  const mat = Array.from({ length: n }, () => input[idx++].split(''));
  const visited = Array.from({ length: n }, () => Array(m).fill(false));
  let firePos = [];
  let currentPos = [];

  // 유효한 범위 확인
  function isValidScope(x, y) {
    return 0 <= x && x < n && 0 <= y && y < m;
  }

  // 불이 번진다
  function fireMove() {
    const nextFirePos = [];
    while (firePos.length) {
      const [x, y] = firePos.pop();

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (isValidScope(nx, ny) && ['.', '@'].includes(mat[nx][ny])) {
          mat[nx][ny] = '*';
          nextFirePos.push([nx, ny]);
        }
      }
    }
    firePos = nextFirePos;
  }

  // 초기 위치 찾기
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (mat[i][j] === '*') {
        firePos.push([i, j]);
      } else if (mat[i][j] === '@') {
        visited[i][j] = true;
        currentPos = [i, j];
      }
    }
  }

  function move() {
    let prevCnt = -1;
    const queue = new Queue();
    queue.push([...currentPos, 0]);
    while (!queue.isEmpty()) {
      const [x, y, cnt] = queue.shift();

      if (prevCnt !== cnt) {
        fireMove();
        prevCnt = cnt;
      }

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        // 탈출하는 경우
        if (!isValidScope(nx, ny)) {
          result.push(cnt + 1);
          return;
        }

        // 빌딩 내부에서 이동하는 경우
        if (mat[nx][ny] === '.' && !visited[nx][ny]) {
          visited[nx][ny] = true;
          queue.push([nx, ny, cnt + 1]);
        }
      }
    }
    result.push('IMPOSSIBLE');
  }

  move();
}
console.log(result.join('\n'));
