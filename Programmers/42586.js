// 스택,큐 - 기능개발
function solution(progresses, speeds) {
    let ans = [];
    let cnt = 0;
    let i = 0;
    const len = progresses.length;
    while (i < len) {
        if (progresses[i] >= 100) {
            cnt++;
            i++;
            continue;
        }
        ans.push(cnt);
        cnt = 1;
        let x = progresses[i];
        const leftday = Math.ceil((100 - x) / speeds[i]);
        for (let j = i + 1; j < len; j++) {
            progresses[j] += speeds[j] * leftday;
        }
        i++;
    }
    ans.push(cnt);
    return ans.slice(1);
}