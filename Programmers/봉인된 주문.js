function solution(n, bans) {
  const sortedBans = bans.sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }

    return a.length - b.length;
  });

  function charToNumber(char) {
    return char.charCodeAt() - 'a'.charCodeAt() + 1;
  }

  let m = n;
  for (let i = 0; i < sortedBans.length; i++) {
    let res = 0;
    for (let c of sortedBans[i]) {
      const charCode = c.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
      res = res * 26 + charCode;
    }

    if (res <= m) {
      m++;
    } else {
      break;
    }
  }

  let ans = '';
  while (m > 0) {
    m--;
    const charCode = (m % 26) + 'a'.charCodeAt(0);
    ans = String.fromCharCode(charCode) + ans;
    m = Math.floor(m / 26);
  }

  return ans;
}
