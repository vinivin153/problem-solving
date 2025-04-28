const input = require('fs')
  .readFileSync('input.txt', 'utf8')
  .trim()
  .split('\n');

const [n, k] = input[0].split(' ').map(Number);
const nums = input[1].split(' ').map(Number);

let [s, e] = [0, 0];
let cnt = nums[0] % 2 ? 1 : 0;
let ans = 0;
while (s <= e && e < n) {
  if (cnt <= k) {
    ans = Math.max(e - s + 1 - cnt, ans);

    if (nums[++e] % 2) cnt++;
  } else {
    if (nums[s++] % 2) cnt--;
  }
}
console.log(ans);
