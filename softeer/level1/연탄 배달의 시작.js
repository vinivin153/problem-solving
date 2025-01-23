const rl = require("readline").createInterface({
  input: process.stdin,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
  n = Number(lines[0]);
  villages = lines[1].split(" ").map(Number);

  let minDist = 1000001;
  let ans = 1;
  for (let i = 1; i < n; i++) {
    const diff = villages[i] - villages[i - 1];
    if (diff < minDist) {
      minDist = diff;
      ans = 1;
    } else if (diff === minDist) {
      ans++;
    }
  }
  console.log(ans);
});
