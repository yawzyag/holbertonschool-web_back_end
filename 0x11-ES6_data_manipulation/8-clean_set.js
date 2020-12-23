const cleanSet = (set, startString) => {
  if (!startString || startString.length < 1) return '';

  let string = '';
  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      string += `-${element.slice(startString.length)}`;
    }
  });
  return string.substring(1);
};
export default cleanSet;
