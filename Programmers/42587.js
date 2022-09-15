// 스택/큐 - 프린터
function solution(priorities, location) {
    let sortedPrior = [...priorities].sort((a, b) => b - a);
    priorities = priorities.map((element, idx) => [element, idx]);
    let cnt = 0;
    while (priorities.length > 0) {
        let [x, idx] = priorities.shift();
        if (x >= sortedPrior[0]) {
            cnt++;
            sortedPrior.shift();
            if (idx === location)
                return cnt;
        } else {
            priorities.push([x, idx]);
        }
    }
}