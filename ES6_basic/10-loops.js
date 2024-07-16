export default function appendToEachArrayValue(array, appendString) {
  for (let i of array) {
    i = appendString + i;
  }
  return array;
}
