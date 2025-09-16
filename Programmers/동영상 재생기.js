function solution(video_len, pos, op_start, op_end, commands) {
  function stringToNumber(time) {
    const [mm, ss] = time.split(':').map(Number);
    return mm * 60 + ss;
  }

  let curr = stringToNumber(pos);
  const start = 0;
  const end = stringToNumber(video_len);
  const ops = stringToNumber(op_start);
  const ope = stringToNumber(op_end);

  // 스킵하는 부분
  if (ops <= curr && curr <= ope) {
    curr = ope;
  }

  for (let command of commands) {
    if (command === 'next') {
      curr += 10;
      if (curr > end) curr = end;
    } else {
      curr -= 10;
      if (start > curr) curr = 0;
    }

    // 스킵하는 부분
    if (ops <= curr && curr <= ope) {
      curr = ope;
    }
  }

  const m = String(Math.floor(curr / 60));
  const s = String(curr % 60);

  return `${m.padStart(2, '0')}:${s.padStart(2, '0')}`;
}
