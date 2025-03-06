const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const edges = Array.from({ length: n + 1 }, () => []);
input.slice(1).map((line) => {
  const [a, b, c] = line.split(' ').map(Number);
  edges[a].push([b, c]);
  edges[b].push([a, c]);
});
const dist = Array(n + 1).fill(Infinity);
const visited = Array(n + 1).fill(false);
const parent = Array(n + 1).fill(-1);

function findMinNode() {
  let minValue = Infinity;
  let idx = -1;
  for (let i = 1; i <= n; i++) {
    if (minValue > dist[i] && !visited[i]) {
      minValue = dist[i];
      idx = i;
    }
  }
  return idx;
}

function dijkstra() {
  dist[1] = 0;
  const stack = [[0, 1]];
  while (stack.length) {
    const minNode = findMinNode();

    if (minNode === -1) break;

    visited[minNode] = true;

    for (let [nextNode, nextDist] of edges[minNode]) {
      if (dist[minNode] + nextDist < dist[nextNode]) {
        dist[nextNode] = dist[minNode] + nextDist;
        parent[nextNode] = minNode;
      }
    }
  }
}

dijkstra();
const ans = [];
for (let i = 2; i <= n; i++) {
  ans.push(i + ' ' + parent[i]);
}
console.log(n - 1);
console.log(ans.join('\n'));
