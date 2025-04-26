class Node {
  constructor(value, next) {
    this.value = value;
    this.next = next;
  }
}

class Queue {
  head;
  tail;

  isEmpty() {
    return !this.head;
  }

  push(element) {
    const node = new Node(element, null);
    if (this.head) this.tail.next = node;
    else this.head = node;
    this.tail = node;
  }

  shift() {
    if (this.isEmpty()) return null;

    const res = this.head.value;
    this.head = this.head.next;
    return res;
  }
}

const input = require('fs')
  .readFileSync('input.txt', 'utf8')
  .trim()
  .split('\n');

function trans(num, c) {
  switch (c) {
    case 'D':
      return (num * 2) % 10000;
    case 'S':
      return num === 0 ? 9999 : num - 1;
    case 'L': {
      const firstDigit = Math.floor(num / 1000);
      const remain = num % 1000;
      return remain * 10 + firstDigit;
    }
    case 'R': {
      const lastDigit = num % 10;
      const remain = Math.floor(num / 10);
      return lastDigit * 1000 + remain;
    }
    default:
      return null;
  }
}

const ans = [];
const t = Number(input[0]);
for (let tc = 1; tc <= t; tc++) {
  const [a, b] = input[tc].split(' ').map(Number);

  const visited = Array(10000).fill(false);
  visited[a] = true;

  const queue = new Queue();
  queue.push([a, '']);
  outerLoop: while (!queue.isEmpty()) {
    const [n, command] = queue.shift();

    for (let c of ['D', 'S', 'L', 'R']) {
      const res = trans(n, c);

      if (res === b) {
        ans.push(command + c);
        break outerLoop;
      }

      if (!visited[res]) {
        visited[res] = true;
        queue.push([res, command + c]);
      }
    }
  }
}

console.log(ans.join('\n'));
