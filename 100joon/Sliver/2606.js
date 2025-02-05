const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");

const n = Number(input[0]);
const m = Number(input[1]);

const edges = Array.from({ length: n + 1 }, () => []);
for (let i = 0; i < m; i++) {
  const [a, b] = input[i + 2].split(" ").map(Number);
  edges[a].push(b);
  edges[b].push(a);
}

let ans = 0;
const stack = [];
const visited = Array(n + 1).fill(false);
visited[1] = true;
stack.push(1);
while (stack.length) {
  x = stack.pop();

  for (let i of edges[x]) {
    if (!visited[i]) {
      visited[i] = true;
      ans += 1;
      stack.push(i);
    }
  }
}

console.log(ans);
