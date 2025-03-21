const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const n = Number(input[0]);
const nums = input[1].split(' ').map(Number);

let ans = 0;
let [left, right] = [0, n - 1];
while (left < right) {
  const cnt = right - left - 1;
  const ability = cnt * Math.min(nums[left], nums[right]);

  ans = Math.max(ans, ability);

  if (nums[left] < nums[right]) {
    left += 1;
  } else {
    right -= 1;
  }
}

console.log(ans);
