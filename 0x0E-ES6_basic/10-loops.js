export default function appendToEachArrayValue(array, appendString) {
  for (const [i, v] of array.entries()) {
    // eslint-disable-next-line no-param-reassign
    array[i] = appendString + v;
  }

  return array;
}
