// const sleep = (wait) => {
//   return new Promise((resolve) => {
//     setTimeout(resolve, wait);
//   });
// };

const sleep = (wait) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("hello");
    }, wait);
  });
};
