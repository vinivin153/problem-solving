const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

let idx = 0;
const t = Number(input[idx++]);
const ans = [];
for (let tc = 0; tc < t; tc++) {
  const n = Number(input[idx++]);
  const nums = [0, ...input[idx++].split(' ').map(Number)];
  const visited = Array(n + 1).fill(false);
  let result = n;

  function dfs(origin) {
    const stack = [];
    const history = new Map();
    history.set(origin, 0);
    stack.push([origin, 0]);
    while (stack.length) {
      const [x, cnt] = stack.pop();
      visited[x] = true;
      if (nums[x] === x) {
        return 1;
      }

      if (!visited[nums[x]]) {
        history.set(nums[x], cnt + 1);
        stack.push([nums[x], cnt + 1]);
      } else if (history.has(nums[x]) && cnt) {
        return cnt + 1 - history.get(nums[x]);
      }
    }
    return 0;
  }

  for (let i = 1; i <= n; i++) {
    if (!visited[i]) {
      const res = dfs(i);
      result -= res;
    }
  }
  ans.push(result);
}
console.log(ans.join('\n'));
