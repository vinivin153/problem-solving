const rl = require("readline").createInterface({
  input: process.stdin,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
  const t = Number(lines[0]);
  const numbers = lines[1].split(" ").map(Number);

  let max_value = Infinity * -1;
  for (let i = 0; i < t; i++) {
    for (let j = i + 1; j < t; j++) {
      max_value = Math.max(numbers[i] * numbers[j], max_value);
    }
  }

  console.log(max_value);
});
