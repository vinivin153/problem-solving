const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const n = Number(input[0]);
const level = input[1].split(' ').map(Number);

const mistake = Array(n + 1).fill(0);
const prefix = Array(n + 1).fill(0);
for (let i = 1; i < n; i++) {
  if (level[i - 1] > level[i]) {
    mistake[i] = 1;
  }

  prefix[i] = prefix[i - 1] + mistake[i];
}
prefix[n] = prefix[n - 1];

const ans = [];
const q = Number(input[2]);
for (let i = 3; i < q + 3; i++) {
  const [x, y] = input[i].split(' ').map(Number);
  let diff = prefix[y] - prefix[x - 1];

  if (mistake[y]) diff--;

  ans.push(diff);
}

console.log(ans.join('\n'));
