const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const [n, r, c] = input[0].split(' ').map(Number);
const N = Math.pow(2, n);

function isInclude(x1, y1, size) {
  return x1 <= r && r < x1 + size && y1 <= c && c < y1 + size;
}

function recursion(size, x, y, num) {
  if (x === r && y === c) {
    console.log(num);
    return;
  }

  const halfSize = size / 2;
  const nextNum = Math.pow(halfSize, 2);

  if (isInclude(x, y, halfSize)) recursion(halfSize, x, y, num);
  else if (isInclude(x, y + halfSize, halfSize))
    recursion(halfSize, x, y + halfSize, num + nextNum);
  else if (isInclude(x + halfSize, y, halfSize))
    recursion(halfSize, x + halfSize, y, num + nextNum * 2);
  else recursion(halfSize, x + halfSize, y + halfSize, num + nextNum * 3);
}

recursion(N, 0, 0, 0);
