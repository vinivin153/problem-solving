const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => lines.push(Number(line))).on("close", () => {
  const t = lines[0];
  for (let i = 1; i <= t; i++) {
    const n = lines[i];

    const five = "++++ ";
    const quotient = Math.floor(n / 5);
    const remainder = n % 5;

    let ans = five.repeat(quotient);
    ans = ans.concat("|".repeat(remainder));
    console.log(ans);
  }
});
