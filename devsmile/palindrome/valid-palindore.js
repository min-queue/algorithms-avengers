/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  var regex = /[^a-z|A-Z|0-9]/g; // 숫자가 아닌 문자열을 선택하는 정규식
  s = s.replace(regex, "").toLowerCase();
  var result = s.split("").reverse().join("");
  return s === result;
};
