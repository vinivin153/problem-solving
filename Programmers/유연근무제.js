function solution(schedules, timelogs, startday) {
  let ans = 0;

  for (let i = 0; i < timelogs.length; i++) {
    let success = 0;
    let limitTime = schedules[i] + 10;
    if (limitTime % 100 >= 60) limitTime += 40;

    for (let j = 0; j < 7; j++) {
      const nowDay = startday + j;
      if ((nowDay - 1) % 7 === 5 || (nowDay - 1) % 7 === 6) continue;

      const time = timelogs[i][j];
      console.log(i, time, limitTime);
      if (time <= limitTime) success++;
      else break;
    }

    if (success >= 5) ans++;
  }

  return ans;
}
