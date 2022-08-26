// 체육복 - Greedy
function solution(n, lost, reserve) {
    const newReserve = reserve.filter(element => {
        let idx = lost.indexOf(element)
        if (idx !== -1) {
            lost.splice(idx, 1);
        }
        return idx === -1;
    });
    lost.sort((a, b) => { return a - b });
    newReserve.sort((a, b) => { return a - b });
    let cnt = n - lost.length;
    lost.forEach(element => {
        if (newReserve.indexOf(element - 1) !== -1) {
            newReserve.splice(newReserve.indexOf(element - 1), 1);
            cnt += 1;
        }
        else if (newReserve.indexOf(element + 1) !== -1) {
            newReserve.splice(newReserve.indexOf(element + 1), 1);
            cnt += 1;
        }
    })
    return cnt;
}