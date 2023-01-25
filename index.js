// 머쓱이보다 키 큰사람
function solution(array, height) {
  let answer = array.filter((item) => item > height);

  return answer.length;
}
