const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const [n, m, l] = input[0].split(' ').map(Number);

if (n === 0) {
  console.log(Math.ceil(l / (m + 1)));
  process.exit();
}

const rest = input[1].split(' ').map(Number);
rest.sort((a, b) => Number(a) - Number(b));

const arr = [0, ...rest, l];
let [left, right] = [
  1,
  arr.reduce((maxDiff, num, idx) => {
    if (idx === 0) return maxDiff;
    return Math.max(maxDiff, num - arr[idx - 1]);
  }),
];

ans = 0;
while (left <= right) {
  const mid = Math.floor((left + right) / 2);

  let cnt = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] - arr[i - 1] > mid) {
      cnt += Math.ceil((arr[i] - arr[i - 1]) / mid) - 1;
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
