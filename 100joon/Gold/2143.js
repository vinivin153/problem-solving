const [[t], [n], a, [m], b] = require('fs')
  .readFileSync(0, 'utf-8')
  .trim()
  .split('\n')
  .map((line) => line.split(' ').map(Number));

let ans = 0;
const itemsB = new Map();

for (let i = 0; i < m; i++) {
  let acc = 0;
  for (let j = i; j < m; j++) {
    acc += b[j];
    itemsB.set(acc, (itemsB.get(acc) || 0) + 1);
  }
}

for (let i = 0; i < n; i++) {
  let acc = 0;
  for (let j = i; j < n; j++) {
    acc += a[j];
    const diff = t - acc;
    if (itemsB.has(diff)) {
      ans += itemsB.get(diff);
    }
  }
}

console.log(ans);
