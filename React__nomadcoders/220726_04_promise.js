// -----------비동기는 언제끝날지 예측이 불가하다.그래서 콜백이 필요함
// -----------그래서 순서제어때문에 콜백을 썼더니 콜백지옥주의...
// -----------콜백지옥에서 벗어나려고 "promise" '.then.catch.finally'
const printString = (string) => {
  return new Promise((resolve, reject) => {
    //reject에러가 있을경우엔, try,catch문으로 잡아주기.
    setTimeout(() => {
      console.log(string);
      resolve();
    }, Math.floor(Math.random() * 100) + 1);
  });
};
//이것이 promise chaining
const printAll = () => {
  printString("A")
    .then(() => {
      return printString("B");
    })
    .then(() => {
      return printString("C");
    });
}; //마지막 .catch로 모든에러를 한번에 잡을 수 있다!!
//return처리를 안하면 또 promiseHell주의 ㅋㅋㅋ
printAll();
