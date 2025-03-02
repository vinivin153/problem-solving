const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const n = Number(input[0]);
const items = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);

let [front, rear] = [0, n - 1];
let [ansValue, ansItem1, ansItem2] = Array(3).fill(Infinity);

while (front < rear) {
  const mixValue = items[front] + items[rear];
  if (Math.abs(mixValue) < Math.abs(ansValue)) {
    [ansValue, ansItem1, ansItem2] = [mixValue, items[front], items[rear]];

    if (ansValue === 0) break;
  }

  if (mixValue < 0) {
    front++;
  } else {
    rear--;
  }
}

console.log(ansItem1, ansItem2);
