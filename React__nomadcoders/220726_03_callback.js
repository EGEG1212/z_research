[1, 2, 3].map(function (el, index) {
  return el * el;
});

//한줄로표현
[1, 2, 3].map((el, index) => el * el);

//DOM에서
document.querySelector("#btn").addEventListener("click", function (e) {
  console.log("버튼이클릭되었습니다.");
});

// -----------비동기는 언제끝날지 예측이 불가하다.그래서 콜백이 필요함
// -----------그래서 순서제어때문에 콜백을 썼더니 콜백지옥주의...
const printString = (string, callback) => {
  setTimeout(() => {
    console.log(string);
    callback();
  }, Math.floor(Math.random() * 100) + 1);
};

const printAll = () => {
  printString("A", () => {
    printString("B", () => {
      printString("C", () => {});
    });
  });
};
printAll();

// ----callback error handling Design
const somethingGonnaHappen = (callback) => {
  waitngUntilSomethingHappens();
  if (isSomthingGood) {
    callback(null, something); //보통 에러를 앞에, 데이터결과값
  }
  if (isSomethinBad) {
    callback(something, null); //에러났을경우 결과값을 에러로표시, 데이터결과값은null
  }
};

somethingGonnaHappen((err, data) => {
  if (err) {
    console.log("ERR!!");
    return;
  }
  return data;
});
