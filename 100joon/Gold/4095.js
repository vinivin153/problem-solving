const input = require('fs')
  .readFileSync('input.txt', 'utf-8')
  .trim()
  .split('\n');

let idx = 0;
const res = [];

while (true) {
  const [n, m] = input[idx++].split(' ').map(Number);

  // 종료조건
  if (n === 0 && m === 0) break;

  // 메모리 사용량 최적화: 전체 행렬을 미리 생성하지 않고 행별로 처리
  let ans = 0;
  const dp = new Array(m).fill(0);
  const prevDp = new Array(m).fill(0);

  for (let i = 0; i < n; i++) {
    const row = input[idx++].split(' ').map(Number);
    let leftTop = 0;

    for (let j = 0; j < m; j++) {
      // 이전 dp[j] 값 저장
      const temp = dp[j];

      if (row[j] === 0) {
        dp[j] = 0;
      } else {
        if (i === 0 || j === 0) {
          dp[j] = 1;
        } else {
          dp[j] = Math.min(leftTop, prevDp[j], dp[j - 1]) + 1;
        }
        ans = Math.max(ans, dp[j]);
      }

      // 다음 반복을 위해 leftTop 업데이트
      leftTop = temp;

      // 이전 행의 값 업데이트
      prevDp[j] = dp[j];
    }
  }

  res.push(ans);
}

console.log(res.join('\n'));
