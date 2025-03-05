const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const n = Number(input[0]);
let k = Number(input[1]);
const nums = input[2]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);

const diff = [];
for (let i = 1; i < n; i++) {
  diff.push(nums[i] - nums[i - 1]);
}
diff.sort((a, b) => a - b);

while (--k > 0) {
  diff.pop();
}

const result = diff.reduce((acc, curr) => acc + curr, 0);
console.log(result);
