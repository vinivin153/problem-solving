const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n')
  .map(Number);

const ans = [];
const t = input[0];
for (let tc = 1; tc <= t; tc++) {
  const n = input[tc];
  const s = new Set(Array.from({ length: 10 }, (_, idx) => idx.toString()));
  for (let i = 1; i <= 45; i++) {
    const num = i * n;

    for (let c of num.toString()) {
      if (s.has(c)) {
        s.delete(c);
      }
    }

    if (s.size === 0) {
      ans.push(`Case #${tc}: ${num}`);
      break;
    }
  }
  if (s.size) {
    ans.push(`Case #${tc}: INSOMNIA`);
  }
}

console.log(ans.join('\n'));
