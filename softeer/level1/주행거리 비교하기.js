const rl = require("readline").createInterface({
  input: process.stdin,
});

rl.on("line", (line) => {
  const [a, b] = line.split(" ").map(Number);

  let ans = "";
  if (a === b) {
    ans = "same";
  } else if (a > b) {
    ans = "A";
  } else {
    ans = "B";
  }
  console.log(ans);
});
