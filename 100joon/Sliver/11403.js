const input = require('fs')
  .readFileSync('input.txt', 'utf8')
  .trim()
  .split('\n');

const n = Number(input[0]);
const mat = input.slice(1).map((line) => line.split(' ').map(Number));

for (let m = 0; m < n; m++) {
  for (let s = 0; s < n; s++) {
    for (let e = 0; e < n; e++) {
      if (mat[s][m] && mat[m][e]) {
        mat[s][e] = 1;
      }
    }
  }
}

console.log(mat.map((row) => row.join(' ')).join('\n'));
