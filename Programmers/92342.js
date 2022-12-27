// 양궁대회
function solution(n, info) {
  const ryan = Array(11).fill(0);
  let answer = [-1];
  let value = -1;

  function btk(cnt, k) {
    if (cnt === n) {
      [score1, score2] = [0, 0];

      for (let i = 0; i <= 10; i++) {
        if (info[i] || ryan[i]) {
          if (info[i] < ryan[i]) {
            score2 += 10 - i;
          } else {
            score1 += 10 - i;
          }
        }
      }

      const res = score2 - score1;

      if (res > 0) {
        if (res === value) {
          for (let i = 10; i >= 0; i--) {
            if (answer[i] > ryan[i]) {
              break;
            } else if (answer[i] < ryan[i]) {
              answer = [...ryan];
              value = res;
              break;
            }
          }
        } else if (res >= value) {
          answer = [...ryan];
          value = res;
        }
      }

      return;
    }

    for (let i = k; i <= 10; i++) {
      if (info[i] >= ryan[i]) {
        ryan[i] += 1;
        btk(cnt + 1, i);
        ryan[i] -= 1;
      }
    }
  }

  btk(0, 0);

  return answer;
}
