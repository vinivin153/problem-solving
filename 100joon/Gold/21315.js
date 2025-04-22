const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

const n = Number(input[0]);
const res = input[1].split(' ').map(Number);

function isEqual(arr) {
  return res.every((value, idx) => value === arr[idx]);
}

function shuffle() {
  for (let k1 = 1; k1 <= 9; k1++) {
    let cards = Array.from({ length: n }, (_, idx) => idx + 1);
    const num = 2 ** k1;
    if (num >= n) break;

    cards = [
      ...shuffle2(cards.slice(n - num), 2, k1),
      ...cards.slice(0, n - num),
    ];

    for (let k2 = 1; k2 <= 9; k2++) {
      const num = 2 ** k2;
      if (num >= n) break;

      const result = [
        ...shuffle2(cards.slice(n - num), 2, k2),
        ...cards.slice(0, n - num),
      ];

      if (isEqual(result)) {
        console.log(k1, k2);
        return;
      }
    }
  }
}

function shuffle2(arr, i, k) {
  if (i === k + 1) {
    return [arr[1], arr[0]];
  }

  const num = 2 ** (k - i + 1);
  return [
    ...shuffle2(arr.slice(arr.length - num), i + 1, k),
    ...arr.slice(0, arr.length - num),
  ];
}

shuffle();
