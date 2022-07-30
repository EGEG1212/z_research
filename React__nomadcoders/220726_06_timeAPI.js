setTimeout(function () {
  console.log("1초 후 실행");
}, 1000);

setInterval(function () {
  console.log("1초마다 실행");
}, 1000);

const timer = setInterval(function () {
  console.log("1초마다 실행");
}, 1000);

clearInterval(timer);
///저왜 안멈추죠???😅 아이런...
//각각실행하면 멈춤
