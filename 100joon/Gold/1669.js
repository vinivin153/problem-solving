input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\n');

const [x, y] = input[0].split(' ').map(Number);
const diff = y - x;

n = 0;
while (true) {
  if (Math.pow(n + 1, 2) > diff) {
    break;
  }

  n++;
}

let ans = 2 * n - 1;

k = diff - Math.pow(n, 2);
ans += Math.ceil(k / n);

if (n === 0) {
  ans = 0;
}

console.log(ans);
