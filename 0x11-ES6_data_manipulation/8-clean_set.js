const cleanSet = (set, startString) => {
  if (!startString) return '';

  let string = '';
  set.forEach((element) => {
    if (element && element.startsWith(startString)) {
      string += `-${element.split(startString).pop()}`;
    }
  });
  return string.substring(1);
};
export default cleanSet;
