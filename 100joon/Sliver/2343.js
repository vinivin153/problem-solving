const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const lectures = input[1].split(" ").map(Number);
let ans = Math.max(...lectures);
let [left, right] = [ans, lectures.reduce((acc, curr) => acc + curr)];

while (left <= right) {
  const mid = Math.floor((left + right) / 2);
  let sum = 0;
  let cnt = 1;

  for (let lecture of lectures) {
    if (sum + lecture > mid) {
      sum = lecture;
      cnt += 1;
    } else {
      sum += lecture;
    }
  }

  if (cnt <= m) {
    ans = mid;
    right = mid - 1;
  } else {
    left = mid + 1;
  }
}
console.log(ans);
