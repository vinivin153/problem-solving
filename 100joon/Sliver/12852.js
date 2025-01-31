const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const dp = Array(n + 1).fill(Infinity);
dp[1] = 0;
const history = Array({ length: n + 1 }).map((_, idx) => idx + 1);

for (let x = 2; x <= n; x++) {
  if (x % 3 === 0 && dp[x / 3] + 1 < dp[x]) {
    dp[x] = dp[x / 3] + 1;
    history[x] = x / 3;
  }

  if (x % 2 === 0 && dp[x / 2] + 1 < dp[x]) {
    dp[x] = dp[x / 2] + 1;
    history[x] = x / 2;
  }

  if (dp[x - 1] + 1 < dp[x]) {
    dp[x] = dp[x - 1] + 1;
    history[x] = x - 1;
  }
}
const ans = [n];
let idx = n;
while (idx > 1) {
  ans.push(history[idx]);
  idx = history[idx];
}

console.log(dp[n]);
console.log(...ans);
