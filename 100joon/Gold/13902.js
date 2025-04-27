const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ').map(Number);
const woks = input[1].split(' ').map(Number);

let cook = new Set();
// 웍 1개 혹은 2개로 만들 수 있는 짜장면
for (let i = 0; i < m; i++) {
  cook.add(woks[i]);
  for (let j = i + 1; j < m; j++) {
    cook.add(woks[i] + woks[j]);
  }
}
cook = [...cook].sort((a, b) => a - b);
const dp = Array(n + 1).fill(Infinity);
dp[0] = 0;
for (let i = 1; i <= n; i++) {
  for (let j = 0; j < cook.length; j++) {
    if (i - cook[j] < 0) {
      break;
    }

    dp[i] = Math.min(dp[i], dp[i - cook[j]] + 1);
  }
}

console.log(dp[n] === Infinity ? -1 : dp[n]);
