const readline = require("readline");
const lines = [];
readline
  .createInterface({
    input: process.stdin,
    output: process.stdout,
  })
  .on("line", (line) => {
    lines.push(line);
  })
  .on("close", () => {
    const s = lines[0].split("");
    const t = lines[1].split("");
    let ans = 0;

    while (1) {
      if (t.length === s.length) {
        if (JSON.stringify(t) === JSON.stringify(s)) {
          ans = 1;
        }
        break;
      }
      const last = t.pop();
      if (last === "B") {
        t.reverse();
      }
    }

    console.log(ans);
    process.exit(0);
  });
