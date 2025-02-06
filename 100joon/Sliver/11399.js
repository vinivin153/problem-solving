const input = require("fs")
  .readFileSync("input.txt", "utf-8")
  .trim()
  .split("\n");

const nums = input[1].split(" ").map(Number);
nums.sort((a, b) => a - b);

let sum = 0,
  total = 0;

for (const num of nums) {
  sum += num;
  total += sum;
}

console.log(total);
