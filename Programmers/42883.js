// Greedy - 큰 수 만들기
function solution(number, k) {
    let stack = [];
    stack.push(number[0]);
    for (let i = 1; i < number.length; i++) {
        while (k > 0 && stack.at(-1) < number[i]) {
            stack.pop();
            k--;
        }
        if (k === 0)
            return stack.join("") + number.slice(i);
        stack.push(number[i]);
    }
    return stack.slice(0, stack.length - k).join("");
}