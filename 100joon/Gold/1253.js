const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const n = Number(input[0]);
const nums = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);
let ans = 0;

for (let i = 0; i < n; i++) {
  bs(i);
}

function bs(target) {
  let [left, right] = [0, n - 1];
  while (left < right) {
    let sum = nums[left] + nums[right];
    if (sum === nums[target]) {
      if (left !== target && right !== target) {
        ans += 1;
        return;
      }
      if (left === target) left++;
      if (right === target) right--;
      continue;
    }

    if (sum > nums[target]) {
      right--;
    } else {
      left++;
    }
  }
}

console.log(ans);
