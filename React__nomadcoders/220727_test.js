//배열 작성
const arrFunc = [];
for (let i = 0; i < 5; i++) {
  const func = (resolve) => {
    console.log(`처리 ${i} 시작`, new Date().toLocaleTimeString());
    // 0~2초 지연
    const delayMsec = 2000 * Math.random();

    // 지연 처리
    setTimeout(() => {
      console.log(`처리 ${i} 완료`, new Date().toLocaleTimeString());
      resolve();
    }, delayMsec);
  };
  // 배열 저장
  arrFunc.push(func);
}

console.log(arrFunc);
