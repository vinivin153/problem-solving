let ipv6 = require('fs').readFileSync(0, 'utf8').trim();

let prev = '';
let doubleColon = false;
let cnt = 0;
for (let i of ipv6) {
  if (prev === ':' && i === ':') {
    cnt--;
    doubleColon = true;
  } else if (i === ':') {
    cnt++;
  }
  prev = i;
}

if (doubleColon) {
  const rv = '0000:';
  ipv6 = ipv6.replace('::', ':' + rv.repeat(6 - cnt));
}

if (ipv6[0] === ':') {
  ipv6 = '0000' + ipv6;
}
if (ipv6[ipv6.length - 1] === ':') {
  ipv6 = ipv6 + '0000';
}

ipv6 = ipv6.split(':');
for (let i = 0; i < ipv6.length; i++) {
  ipv6[i] = ipv6[i].padStart(4, 0);
}
console.log(ipv6.join(':'));
