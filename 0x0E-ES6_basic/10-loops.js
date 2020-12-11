export default function appendToEachArrayValue(array, appendString) {
  const newArr = [];
  for (const v of array) {
    const val = appendString + v;
    newArr.push(val);
  }

  return newArr;
}
