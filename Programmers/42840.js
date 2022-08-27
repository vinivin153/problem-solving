// 모의고사 - 완전탐색
function solution(answers) {
    const a = [1, 2, 3, 4, 5]; // 5개
    const b = [2, 1, 2, 3, 2, 4, 2, 5]; // 8개
    const c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]; // 10개
    let ans = [-1, 0, 0, 0];
    answers.forEach((element, idx) => {
        if (a[idx % 5] === element) {
            ans[1]++;
        }
        if (b[idx % 8] === element) {
            ans[2]++;
        }
        if (c[idx % 10] === element) {
            ans[3]++;
        }
    });
    let res = []
    for (let i = 1; i < 4; i++) {
        if (Math.max(...ans) === ans[i]) {
            res.push(i);
        }
    }
    return res;
}