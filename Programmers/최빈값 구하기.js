function solution(array) {
  const map = new Map();
  for (let i of array) {
    map.set(i, (map.get(i) || 0) + 1);
  }

  const sortedMap = [...map].sort((a, b) => Number(b[1]) - Number(a[1]));

  if (sortedMap.length === 1) return array[0];

  if (sortedMap[0][1] === sortedMap[1][1]) {
    return -1;
  } else {
    return sortedMap[0][0];
  }
}
