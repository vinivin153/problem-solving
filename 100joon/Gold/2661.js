const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
const n = Number(input[0]);
const nums = ["1", "2", "3"];

function isGoodSequence(str) {
  const rear = str.length - 1;
  const half = str.length / 2 - 1;
  let idx = str.length - 2;
  while (half <= idx) {
    let isBad = true;

    for (let i = 0; i < str.length - 1 - idx; i++) {
      if (str[rear - i] !== str[idx - i]) {
        idx -= 1;
        isBad = false;
        break;
      }
    }

    if (isBad) return false;
  }
  return true;
}

function dfs(str) {
  if (!isGoodSequence(str)) {
    return;
  }

  if (n == str.length) {
    console.log(str);
    process.exit();
  }

  for (let i of nums) {
    if (i === str[str.length - 1]) continue;
    dfs(str + i);
  }
}

dfs("1");
