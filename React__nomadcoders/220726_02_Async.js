//비동기적인 카페!🥤 한번에 주문받고, 한번에 메뉴나옴 ㅋ
function waitAsync(callback, ms) {
  setTimeout(callback, ms);
} //특정시간 이후에 callback함수가 실행되게끔 하는 브라우저 내장 기능.
function drink(person, coffee) {
  console.log(person + "는 " + coffee + "를 마십니다");
}
//💛비동기
function orderCoffeeASync(menu, callback) {
  console.log(menu + "가 접수되었습니다.");
  waitAsync(function () {
    callback(menu);
  }, 2000);
}

let customers = [
  {
    name: "Anne",
    request: "쑥떡프라푸치노",
  },
  {
    name: "Json",
    request: "아메리카노",
  },
];

//call Asynchronously + 콜백함수를 넣어봄
customers.forEach(function (customer) {
  orderCoffeeASync(customer.request, function (coffee) {
    drink(customer.name, coffee);
  });
});

// -----------비동기는 언제끝날지 예측이 불가하다.그래서 콜백이 필요함
const printString = (string) => {
  setTimeout(() => {
    console.log(string);
  }, Math.floor(Math.random() * 100) + 1);
};

const printAll = () => {
  printString("A");
  printString("B");
  printString("C");
};
printAll();
