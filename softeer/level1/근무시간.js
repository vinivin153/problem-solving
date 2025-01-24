const rl = require("readline").createInterface({
  input: process.stdin,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
  let totalWorkTime = 0;
  for (let i = 0; i < 5; i++) {
    const [start, end] = lines[i].split(" ");
    const startDate = new Date(`2025-01-01T${start}:00`);
    const endDate = new Date(`2025-01-01T${end}:00`);
    const diffDateMs = endDate - startDate;

    const workTime = diffDateMs / 1000 / 60;
    totalWorkTime += workTime;
  }

  console.log(totalWorkTime);
});
