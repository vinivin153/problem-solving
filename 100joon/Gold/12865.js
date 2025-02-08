const input = require("fs")
  .readFileSync("input.txt", "utf-8")
  .trim()
  .split("\n");

const [n, k] = input[0].split(" ").map(Number);
const bags = [];
const visited = Array(k + 1).fill(new Set());
for (let i = 0; i < n; i++) {
  const [w, v] = input[i + 1].split(" ").map(Number);
  bags.push([i, w, v]);
}

bags.sort((a, b) => a[1] - b[1]);

const dp = Array(k + 1).fill(0);
for (let i = 1; i <= k; i++) {
  for (let [idx, w, v] of bags) {
    if (i - w < 0) break;

    const q = dp[i - w] + v;
    if (!visited[i - w].has(idx) && dp[i] < q) {
      visited[i] = new Set([...visited[i - w], idx]);
      dp[i] = q;
    }
  }
}

console.log(Math.max(...dp));
