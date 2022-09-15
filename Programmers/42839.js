// 완전탐색 - 소수찾기
function solution(numbers) {
    let ans = new Set();
    const maxNum = 10000000;
    let sieve = new Array(maxNum).fill(true);

    function eratos() {
        const m = Math.sqrt(maxNum);
        [sieve[0], sieve[1]] = [false, false];

        for (let i = 2; i < m; i++) {
            if (sieve[i] === true) {
                for (let j = i + i; j < maxNum; j += i) {
                    sieve[j] = false;
                }
            }
        }
    }
    let nums = [...numbers];
    let visited = new Array(10).fill(false);

    function dfs(val) {
        let intVal = parseInt(val, 10);
        if (sieve[intVal] && !ans.has(intVal)) {
            ans.add(intVal);
        }
        for (let i = 0; i < nums.length; i++) {
            if (visited[i] === false) {
                visited[i] = true;
                dfs(val + nums[i]);
                visited[i] = false;
            }
        }
    }
    eratos();
    dfs("");

    return ans.size;
}