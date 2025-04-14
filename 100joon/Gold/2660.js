input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\n');

const n = Number(input[0]);
let idx = 1;
const rel = Array.from({ length: n + 1 }, () => []);

while (true) {
  const [a, b] = input[idx++].split(' ').map(Number);

  if (a === -1 && b === -1) {
    break;
  }

  rel[a].push(b);
  rel[b].push(a);
}

let minScore = 50;
let ans = [];
for (let i = 1; i <= n; i++) {
  const result = bfs(i);

  if (minScore === result) {
    ans.push(i);
  } else if (result < minScore) {
    minScore = result;
    ans = [i];
  }
}

console.log(minScore, ans.length);
console.log(ans.join(' '));

function bfs(a) {
  const queue = [];
  queue.push([a, 0]);
  const visited = new Set();
  visited.add(a);
  let depth = 0;

  while (queue.length) {
    const [x, cnt] = queue.shift();
    depth = cnt;

    for (let i of rel[x]) {
      if (!visited.has(i)) {
        visited.add(i);
        queue.push([i, cnt + 1]);
      }
    }
  }

  return depth;
}
