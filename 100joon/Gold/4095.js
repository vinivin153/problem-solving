const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

let idx = 0;
while (true) {
  const [n, m] = input[idx++].split(' ').map(Number);

  // 종료조건
  if (n === 0 && m === 0) break;

  const mat = Array.from({ length: n }, () =>
    input[idx++].split(' ').map(Number)
  );

  const dp = Array.from({ length: n }, () => Array(m).fill(0));
  let ans = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (mat[i][j] === 0) {
        dp[i][j] = 0;
        continue;
      }

      if (0 <= i - 1 && 0 <= j - 1) {
        dp[i][j] = Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1;
      } else {
        dp[i][j] = 1;
      }

      ans = Math.max(ans, dp[i][j]);
    }
  }
  console.log(ans);
}
