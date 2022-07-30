//동기적인 카페. 킹받
function waitSync(ms) {
  var start = Date.now();
  var now = start;
  while (now - start < ms) {
    now = Date.now();
  }
}

function drink(person, coffee) {
  console.log(person + "는 " + coffee + "를 마십니다");
}

function orderCoffeeSync(coffee) {
  console.log(coffee + "가 접수되었습니다");
  waitSync(2000);
  return coffee;
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

//call synchronously
customers.forEach(function (customer) {
  let coffee = orderCoffeeSync(customer.request);
  drink(customer.name, coffee);
});

// 쑥떡프라푸치노가 접수되었습니다
// Anne는 쑥떡프라푸치노를 마십니다
// 아메리카노가 접수되었습니다
// Json는 아메리카노를 마십니다
