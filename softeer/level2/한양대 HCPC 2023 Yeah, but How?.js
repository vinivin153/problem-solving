const input = require("fs").readFileSync(0, "utf-8").trim();

const stack = [];
let t1 = "(";

for (let i = 1; i < input.length; i++) {
  if (input[i] == ")" && input[i - 1] === "(") {
    t1 += 1;
  }

  t1 += input[i];
}

let t2 = "";
for (let i = 0; i < t1.length; i++) {
  if (t1[i - 1] === ")" && t1[i] === "(") {
    t2 += "+";
  }
  t2 += t1[i];
}

console.log(t2);
