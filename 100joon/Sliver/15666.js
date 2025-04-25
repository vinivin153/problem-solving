const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

const [n, m] = input[0].split(' ').map(Number);
const numSet = new Set(input[1].split(' ').map(Number));
const sortedNums = [...numSet].sort((a, b) => a - b);
const res = new Set();

function backtracking(comb, idx) {
  if (comb.length === m) {
    const sortedComb = comb.sort((a, b) => Number(a) - Number(b));
    res.add(sortedComb.join(' '));

    return;
  }

  for (let i = idx; i < sortedNums.length; i++) {
    backtracking([...comb, sortedNums[i]], i);
  }
}

backtracking([], 0);
const ans = [...res];
console.log(ans.join('\n'));
