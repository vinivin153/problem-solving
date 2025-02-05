const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");

const n = Number(input[0]);
const mat = Array.from({ length: n }, () => Array(n).fill(0));

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    mat[i][j] = i + 1;
  }
}

for (let i of mat) {
  console.log(i.join(" "));
}
