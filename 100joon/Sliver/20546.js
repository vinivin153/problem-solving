const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
const n = Number(input[0]);
const stocks = input[1].split(" ").map(Number);

let [junhyun_stock, sungmin_stock] = [0, 0];
let [junhyun_money, sungmin_money] = [n, n];

for (let stock of stocks) {
  if (stock <= junhyun_money) {
    junhyun_stock = Math.floor(n / stock);
    junhyun_money -= junhyun_stock * stock;
    break;
  }
}

let [downDays, upDays] = [0, 0];
for (let day = 1; day < 14; day++) {
  if (stocks[day - 1] < stocks[day]) {
    downDays = 0;
    upDays += 1;

    if (upDays >= 3) {
      sungmin_money += sungmin_stock * stocks[day];
      sungmin_stock = 0;
    }
  } else if (stocks[day - 1] > stocks[day]) {
    upDays = 0;
    downDays += 1;

    if (downDays >= 3) {
      const buyStockCount = Math.floor(sungmin_money / stocks[day]);
      sungmin_stock += buyStockCount;
      sungmin_money -= buyStockCount * stocks[day];
    }
  } else {
    upDays = 0;
    downDays = 0;
  }
}

const junhyun = junhyun_stock * stocks[13] + junhyun_money;
const sungmin = sungmin_stock * stocks[13] + sungmin_money;

if (junhyun > sungmin) {
  console.log("BNP");
} else if (junhyun < sungmin) {
  console.log("TIMING");
} else {
  console.log("SAMESAME");
}
