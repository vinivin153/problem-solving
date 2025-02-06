const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");

const n = Number(input[0]);
const nums = input[1].split(" ").map(Number);

let ans = 0;
let preMax = 0;

for (let i = 0; i < n - 1; i++) {
  if (preMax > nums[i]) continue;

  let cnt = 0;
  for (let j = i + 1; j < n; j++) {
    if (nums[i] > nums[j]) {
      cnt++;
    } else {
      preMax = Math.max(nums[i], preMax);
      break;
    }
  }
  ans = Math.max(ans, cnt);
}

console.log(ans);
