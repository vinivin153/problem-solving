class MaxHeap {
  constructor() {
    this.heap = [];
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  add(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  bubbleUp() {
    let idx = this.heap.length - 1;
    let parentIdx = Math.floor((idx - 1) / 2);
    while (0 < idx && this.heap[idx] > this.heap[parentIdx]) {
      this.swap(idx, parentIdx);
      idx = parentIdx;
      parentIdx = Math.floor((idx - 1) / 2);
    }
  }

  pop() {
    if (this.heap.length === 0) return 0;
    if (this.heap.length === 1) return this.heap.pop();

    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return max;
  }

  bubbleDown() {
    let idx = 0;
    let left = idx * 2 + 1;
    let right = idx * 2 + 2;

    while (left < this.heap.length) {
      let bigger = left;
      if (right < this.heap.length && this.heap[bigger] < this.heap[right]) {
        bigger = right;
      }

      if (this.heap[bigger] < this.heap[idx]) break;

      this.swap(idx, bigger);
      idx = bigger;
      left = idx * 2 + 1;
      right = idx * 2 + 2;
    }
  }
}

const input = require('fs')
  .readFileSync(0, 'utf-8')
  .trim()
  .split('\n')
  .map(Number);

const n = input[0];
const ans = [];
const heap = new MaxHeap();
for (let i = 1; i <= n; i++) {
  const x = input[i];

  if (x === 0) ans.push(heap.pop());
  else heap.add(x);
}

console.log(ans.join('\n'));
