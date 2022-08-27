// 완주하지 못한 선수 - 해시
function solution(participant, completion) {
    let person = {}
    for (let p of participant) {
        p in person ? person[p]++ : person[p] = 1
    }
    for (let p of completion) {
        person[p]--;
    }
    for (let p in person) {
        if (person[p] > 0)
            return p;
    }
}