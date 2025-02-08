const input = require("fs")
  .readFileSync("input.txt", "utf-8")
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const edges = input.slice(1).map((edge) => edge.split(" ").map(Number));
const parent = Array.from({ length: n }, (_, idx) => idx);

function findParent(x) {
  if (parent[x] !== x) {
    parent[x] = findParent(parent[x]);
  }

  return parent[x];
}

function union(x, y) {
  const parentX = findParent(x);
  const parentY = findParent(y);

  if (parentX === parentY) return;

  if (parentX < parentY) {
    parent[parentY] = parentX;
  } else {
    parent[parentX] = parentY;
  }
}

function isCycle(x, y) {
  return findParent(x) === findParent(y);
}

let ans = 0;
for (let i = 0; i < m; i++) {
  const [v1, v2] = edges[i];
  if (isCycle(v1, v2)) {
    ans = i + 1;
    break;
  }

  union(v1, v2);
}

console.log(ans);
