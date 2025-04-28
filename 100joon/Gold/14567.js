const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ').map(Number);
const sub = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i <= m; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  sub[b].push(a);
}

const dp = Array(n + 1).fill(1);

for (let i = 1; i <= n; i++) {
  for (let j of sub[i]) {
    dp[i] = Math.max(dp[i], dp[j] + 1);
  }
}

dp.shift();
console.log(dp.join(' '));
