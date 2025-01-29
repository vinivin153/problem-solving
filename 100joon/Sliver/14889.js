const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const ability = input.slice(1).map((line) => line.split(" ").map(Number));
const visited = Array(n).fill(false);
let minDiff = Infinity;

const calcTeamScore = (member) => {
  let score = 0;
  for (let i = 0; i < member.length; i++) {
    for (let j = 0; j < member.length; j++) {
      score += ability[member[i]][member[j]];
    }
  }
  return score;
};

const backtracking = (cnt, idx) => {
  if (cnt === n / 2) {
    const startTeam = [];
    const linkTeam = [];

    for (let i = 0; i < n; i++) {
      visited[i] ? startTeam.push(i) : linkTeam.push(i);
    }

    const startTeamScore = calcTeamScore(startTeam);
    const linkTeamScore = calcTeamScore(linkTeam);

    minDiff = Math.min(minDiff, Math.abs(startTeamScore - linkTeamScore));
    return;
  }

  for (let i = idx; i < n; i++) {
    if (visited[i]) continue;

    visited[i] = true;
    backtracking(cnt + 1, i + 1);
    visited[i] = false;
  }
};

backtracking(0, 0);
console.log(minDiff);
