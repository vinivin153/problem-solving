const rl = require("readline").createInterface({
  input: process.stdin,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
  const [a, b, d] = lines[0].split(" ").map(Number);

  let current_dist = 0;
  let total_time = 0;
  while (current_dist < d) {
    if (current_dist + a >= d) {
      total_time += d - current_dist;
      break;
    }

    // 현재 거리 업데이트
    current_dist += a;
    // 총 걸린 시간 업데이트
    total_time += a + b;
  }

  current_dist = 0;
  while (current_dist < d) {
    if (current_dist + b >= d) {
      total_time += d - current_dist;
      break;
    }

    current_dist += b;
    total_time += a + b;
  }

  console.log(total_time);
});
