// 같은 숫자는 싫어 - 스택/큐

function solution(arr) {
    let ans = [arr[0]];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] !== arr[i - 1]) {
            ans.push(arr[i]);
        }
    }
    return ans;
}