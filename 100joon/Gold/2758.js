const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

const t = Number(input[0]);

const dp = Array.from({ length: 11 }, () => Array(2001).fill(0));
dp[0].fill(1);
for (let i = 1; i <= 10; i++) {
  for (let j = 1; j <= 2000; j++) {
    dp[i][j] = dp[i][j - 1] + dp[i - 1][Math.floor(j / 2)];
  }
}

const ans = [];
for (tc = 1; tc <= t; tc++) {
  const [n, m] = input[tc].split(' ').map(Number);
  ans.push(dp[n][m]);
}
console.log(ans.join('\n'));
