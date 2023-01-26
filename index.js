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
