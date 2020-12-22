const cleanSet = (set, startString) => {
  if (!startString) return '';

  const string = [...set]
    .map((item) => (item.startsWith(startString) ? item.split(startString).pop() : ''))
    .filter((item) => item)
    .join('-');
  return string;
};
export default cleanSet;
