function solution(n, w, num) {
  const boxLevel = Math.floor((n - 1) / w);
  const boxOffset = boxLevel % 2 ? w - 1 - ((n - 1) % w) : (n - 1) % w;

  const myLevel = Math.floor((num - 1) / w);
  const myOffset = myLevel % 2 ? w - 1 - ((num - 1) % w) : (num - 1) % w;

  let ans = boxLevel - myLevel + 1;
  if (boxLevel % 2 === 0 && myOffset > boxOffset) ans--;
  else if (boxLevel % 2 === 1 && myOffset < boxOffset) ans--;

  return ans;
}
