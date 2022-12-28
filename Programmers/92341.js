// 주차 요금 계산
function solution(fees, records) {
  const MAX_TIME = 23 * 60 + 59;
  const [baseTime, baseFee, unitTime, unitFee] = fees;
  const parkingLot = {};
  const totalParkingTime = {};
  const answer = [];

  records.forEach((record) => {
    const [time, number, move] = record.split(' ');
    let [hh, mm] = time.split(':');
    mm = hh * 60 + Number(mm);

    if (move === 'IN') {
      parkingLot[number] = mm;
    } else {
      const pt = mm - parkingLot[number];
      number in totalParkingTime
        ? (totalParkingTime[number] += pt)
        : (totalParkingTime[number] = pt);
      parkingLot[number] = null;
    }
  });

  for (let number in parkingLot) {
    if (parkingLot[number] !== null) {
      const pt = MAX_TIME - parkingLot[number];
      number in totalParkingTime
        ? (totalParkingTime[number] += pt)
        : (totalParkingTime[number] = pt);
    }
  }

  for (let number in totalParkingTime) {
    if (totalParkingTime[number] <= baseTime) {
      answer.push({ number: number, fee: baseFee });
    } else {
      const overTime = totalParkingTime[number] - baseTime;
      answer.push({
        number: number,
        fee: Math.ceil(overTime / unitTime) * unitFee + baseFee,
      });
    }
  }

  answer.sort((a, b) => a.number - b.number);

  return answer.map((element) => element.fee);
}
