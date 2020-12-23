const cleanSet = (set, startString) => {
  if (!startString) return '';

  let string = '';
  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      string += `-${element.slice(startString.length)}`;
    }
  });
  return string.slice(1, string.length);
};
export default cleanSet;
