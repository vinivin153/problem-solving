const rl = require("readline").createInterface({
  input: process.stdin,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
  const t = Number(lines[0]);

  for (let i = 1; i <= t; i++) {
    const ans = lines[i]
      .split(" ")
      .map(Number)
      .reduce((acc, curr) => acc + curr);
    console.log(`Case #${i}: ${ans}`);
  }
});
