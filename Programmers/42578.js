// 해시 - 위장
function solution(clothes) {
    var answer = 1;
    let dress = {};
    clothes.forEach((cloth) => {
        if (dress[cloth[1]] === undefined) {
            dress[cloth[1]] = 1;
        } else {
            dress[cloth[1]]++;
        }
    });

    Object.keys(dress).forEach(element => {
        answer *= (dress[element] + 1);
    })
    return answer - 1;
}