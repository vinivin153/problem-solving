const input = require('fs')
  .readFileSync('input.txt', 'utf8')
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ').map(Number);
const memory = input[1].split(' ').map(Number);
const cost = input[2].split(' ').map(Number);

const MAX_COST = cost.reduce((acc, curr) => acc + curr, 0);
const dp = Array.from({ length: n + 1 }, () => Array(MAX_COST + 1).fill(0));

let ans = Infinity;
for (let i = 1; i <= n; i++) {
  for (let j = 0; j <= MAX_COST; j++) {
    if (j - cost[i - 1] < 0) {
      dp[i][j] = dp[i - 1][j];
    } else {
      dp[i][j] = Math.max(
        dp[i - 1][j - cost[i - 1]] + memory[i - 1],
        dp[i - 1][j]
      );
    }

    if (dp[i][j] >= m) {
      ans = Math.min(ans, j);
    }
  }
}

console.log(ans);
