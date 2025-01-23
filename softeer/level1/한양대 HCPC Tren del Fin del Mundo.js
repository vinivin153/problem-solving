const rl = require("readline").createInterface({
  input: process.stdin,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
  const n = lines[0];
  let ans = [1001, 1001];
  const arr = lines.slice(1).map((line) => line.split(" ").map(Number));
  for (let item of arr) {
    if (ans[1] > item[1]) {
      ans = item;
    }
  }
  console.log(...ans);
});

// 최적화 버전
// ans = arr.reduce((min, cur) => (min[1] > cur[1] ? cur : min), [1001, 1001]);
