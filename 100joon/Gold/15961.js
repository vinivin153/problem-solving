const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");

const [n, d, k, c] = input[0].split(" ").map(Number);
const fish = [];
for (let i = 0; i < n; i++) {
  fish.push(Number(input[i + 1]));
}
const countFish = Array(d + 1).fill(0);
for (let i = 0; i < k; i++) {
  countFish[fish[i]]++;
}

const set = new Set(fish.slice(0, k));
let ans = set.size;
let [start, end] = [k - 1, 0];
while (true) {
  if (!set.has(c)) {
    ans = Math.max(ans, set.size + 1);
  } else {
    ans = Math.max(ans, set.size);
  }

  countFish[fish[end]] -= 1;
  if (countFish[fish[end]] === 0) {
    set.delete(fish[end]);
  }
  end++;

  start = (start + 1) % n;
  countFish[fish[start]] += 1;
  set.add(fish[start]);

  if (end === n) {
    break;
  }
}
console.log(ans);
