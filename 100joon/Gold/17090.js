const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ').map(Number);
const mat = input.slice(1).map((row) => row.split(''));
let pos = new Set();
let impos = new Set();

const d = {
  U: [-1, 0],
  R: [0, 1],
  D: [1, 0],
  L: [0, -1],
};

function isEscape(r, c) {
  return r < 0 || r >= n || c < 0 || c >= m || pos.has((r + 1) * m + c);
}

function move(r, c) {
  const stack = [];
  stack.push([r, c]);
  const visited = new Set();
  while (stack.length) {
    const [x, y] = stack.pop();
    visited.add((x + 1) * m + y);

    const [dx, dy] = d[mat[x][y]];
    const [nx, ny] = [x + dx, y + dy];

    // 탈출하는 경우
    if (isEscape(nx, ny)) {
      visited.forEach((v) => pos.add(v));
      return;
    }

    // 탈출 불가능한 경우
    const v = (nx + 1) * m + ny;
    if (impos.has(v)) {
      visited.add(v);
      visited.forEach((v) => impos.add(v));
      return;
    }

    if (visited.has(v)) continue;
    stack.push([nx, ny]);
  }

  // 탈출 못 한 경우
  visited.forEach((v) => impos.add(v));
}

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    const v = (i + 1) * m + j;
    if (pos.has(v) || impos.has(v)) continue;

    move(i, j);
  }
}

console.log(pos.size);
