// -----------비동기는 언제끝날지 예측이 불가하다.그래서 콜백이 필요함
// -----------그래서 순서제어때문에 콜백을 썼더니 콜백지옥주의...
// -----------콜백지옥에서 벗어나려고 "promise" '.then.catch.finally'
//promise와 비동기적으로 돌아가는데 표현을 동기적으로 할 수 있어서 "async와 await"를 쓴다
function gotoFarm() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("🦃");
    }, 500);
  });
}

function getEgg() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("🥚");
    }, 400);
  });
}

function eatLunch() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("🍳");
    }, 300);
  });
}

function ImHappy() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("😋");
    }, 500);
  });
}

const result = async () => {
  const one = await gotoFarm();
  console.log(one);

  const two = await getEgg();
  console.log(two);

  const three = await eatLunch();
  console.log(three);

  const four = await ImHappy();
  console.log(four);
};

result();
