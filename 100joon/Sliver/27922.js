const readline = require("readline");
const lines = [];
let ans = 0;

readline
  .createInterface({
    input: process.stdin,
    output: process.stdout,
  })
  .on("line", (line) => {
    lines.push(line);
  })
  .on("close", () => {
    const [n, k] = lines[0].split(" ").map(Number);
    const subjects = lines.slice(1, n + 1).map((l) => l.split(" ").map(Number));

    const s1 = subjects.slice().sort((a, b) => b[0] + b[1] - (a[0] + a[1]));
    const s2 = subjects.slice().sort((a, b) => b[0] + b[2] - (a[0] + a[2]));
    const s3 = subjects.slice().sort((a, b) => b[1] + b[2] - (a[1] + a[2]));

    const first_val = s1
      .slice(0, k)
      .reduce((acc, item) => acc + item[0] + item[1], 0);
    const second_val = s2
      .slice(0, k)
      .reduce((acc, item) => acc + item[0] + item[2], 0);
    const third_val = s3
      .slice(0, k)
      .reduce((acc, item) => acc + item[1] + item[2], 0);

    ans = Math.max(first_val, second_val, third_val);
    console.log(ans);
    process.exit(0);
  });
