const [n, l, w, h] = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split(' ')
  .map(Number);

let ans = 0;
let [left, right] = [0, Math.max(l, w, h)];
for (let _ = 0; _ < 60; _++) {
  const mid = (left + right) / 2;

  const cnt = Math.floor(l / mid) * Math.floor(w / mid) * Math.floor(h / mid);

  if (cnt < n) {
    right = mid;
  } else {
    ans = mid;
    left = mid;
  }
}

console.log(ans);
