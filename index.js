// 머쓱이보다 키 큰사람
function solution(array, height) {
  let answer = array.filter((item) => item > height);

  return answer.length;
}

//아이스 아메리카노
function solution(money) {
  const americano = 5500;

  const glass = Math.floor(money / americano);
  const exchange = money % americano;

  return [glass, exchange];
}

function a() {}

// 배열의 평균값
function solution(numbers) {
  var answer = 0;
  let sum = 0;

  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return (answer = sum / numbers.length);
}
