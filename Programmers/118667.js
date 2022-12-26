// 두 큐 합 같게 만들기
class Queue {
  constructor(arr) {
    this.queue = arr;
    this.front = 0;
    this.rear = arr.length;
  }

  enqueue(value) {
    this.queue[this.rear++] = value;
  }

  dequeue() {
    const value = this.queue[this.front];
    delete this.queue[this.front];
    this.front++;

    return value;
  }

  size() {
    return this.rear - this.front;
  }

  sum() {
    return this.queue.reduce((acc, num) => acc + num);
  }

  peek() {
    return this.queue[this.front];
  }
}

function solution(queue1, queue2) {
  q1 = new Queue(queue1);
  q2 = new Queue(queue2);

  let sum1 = q1.sum();
  let sum2 = q2.sum();

  if ((sum1 + sum2) % 2) return -1;

  let answer = 0;
  while (sum1 !== sum2) {
    if (sum1 > sum2) {
      const temp = q1.peek();
      q2.enqueue(q1.dequeue());
      sum1 -= temp;
      sum2 += temp;
    } else {
      const temp = q2.peek();
      q1.enqueue(q2.dequeue());
      sum1 += temp;
      sum2 -= temp;
    }

    answer += 1;

    if (answer > 600000) return -1;
  }

  return answer;
}
