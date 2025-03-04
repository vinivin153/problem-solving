const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

const t = Number(input[0]);
let idx = 1;
const result = [];
for (let tc = 0; tc < t; tc++) {
  const f = Number(input[idx++]);
  const parent = new Map();
  const parent_cnt = new Map();

  function findParent(x) {
    if (x !== parent.get(x)) {
      parent.set(x, findParent(parent.get(x)));
    }

    return parent.get(x);
  }

  function union(f1, f2) {
    const f1Parent = findParent(f1);
    const f2Parent = findParent(f2);

    if (f1Parent === f2Parent) return f1Parent;

    if (parent_cnt.get(f1Parent) < parent_cnt.get(f2Parent)) {
      parent.set(f2Parent, f1Parent);
      parent_cnt.set(
        f1Parent,
        parent_cnt.get(f1Parent) + parent_cnt.get(f2Parent)
      );
      return f1Parent;
    } else {
      parent.set(f1Parent, f2Parent);
      parent_cnt.set(
        f2Parent,
        parent_cnt.get(f2Parent) + parent_cnt.get(f1Parent)
      );
      return f2Parent;
    }
  }

  for (let friendIdx = 0; friendIdx < f; friendIdx++) {
    const [friend1, friend2] = input[idx++].split(' ');
    if (!parent.has(friend1)) {
      parent.set(friend1, friend1);
      parent_cnt.set(friend1, 1);
    }
    if (!parent.has(friend2)) {
      parent.set(friend2, friend2);
      parent_cnt.set(friend2, 1);
    }

    result.push(parent_cnt.get(union(friend1, friend2)));
  }
}
console.log(result.join('\n'));
