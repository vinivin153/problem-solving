// 포켓몬 - 해시
function solution(nums) {
    const pick = nums.length / 2;
    const set = new Set(nums);
    const kindOfNums = set.size;

    if (kindOfNums <= pick) {
        return kindOfNums
    } else {
        return pick
    }
}
