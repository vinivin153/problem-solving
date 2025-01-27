const rl = require("readline").createInterface({
  input: process.stdin,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
  const [n, m] = lines[0].split(" ").map(Number);
  const arr = lines[1].split(" ").map(Number);

  let [start, end] = [0, 0];
  let sum = arr[0];
  let ans = 0;
  while (start <= end && end < n) {
    if (sum === m) {
      ans += 1;
      sum += arr[++end];
    } else if (sum < m) {
      sum += arr[++end];
    } else {
      if (start === end) {
        sum += arr[++end];
      }
      sum -= arr[start++];
    }
  }
  console.log(ans);
});
