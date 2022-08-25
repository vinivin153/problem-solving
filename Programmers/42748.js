function solution(array, commands) {
    var answer = [];
    for (let command of commands) {
        let newArr = array.slice(command[0] - 1, command[1]).sort((a, b) => {
            return a - b;
        });
        answer.push(newArr[command[2] - 1]);
    }
    return answer;
}