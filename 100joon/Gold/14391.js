const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const mat = input.slice(1).map((line) => line.split('').map(Number));
let ans = 0;

for (let bitmask = 0; bitmask < 1 << (n * m); bitmask++) {
  let total = 0;
  // 가로
  for (let i = 0; i < n; i++) {
    let rowSum = 0;
    for (let j = 0; j < m; j++) {
      const idx = i * m + j;
      if ((bitmask & (1 << idx)) === 0) {
        rowSum = rowSum * 10 + mat[i][j];
      } else {
        total += rowSum;
        rowSum = 0;
      }
    }
    total += rowSum;
  }

  // 세로
  for (let j = 0; j < m; j++) {
    let colSum = 0;
    for (let i = 0; i < n; i++) {
      const idx = i * m + j;
      if ((bitmask & (1 << idx)) !== 0) {
        colSum = colSum * 10 + mat[i][j];
      } else {
        total += colSum;
        colSum = 0;
      }
    }
    total += colSum;
  }
  if (ans < total) ans = total;
}
console.log(ans);
