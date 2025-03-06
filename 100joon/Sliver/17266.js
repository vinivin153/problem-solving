const input = require('fs')
  .readFileSync(0, 'utf-8')
  .trim()
  .split('\n')
  .map((line) => line.split(' ').map(Number));

const [[n], [m], pos] = input;
const [front, rear] = [pos[0], n - pos[pos.length - 1]];
const gap = pos.reduce((maxDiff, curr, idx) => {
  if (idx === 0) return maxDiff;

  const diff = Math.abs(curr - pos[idx - 1]);
  if (diff > maxDiff) return diff;
  else return maxDiff;
}, 0);

console.log(Math.max(front, rear, Math.ceil(gap / 2)));
