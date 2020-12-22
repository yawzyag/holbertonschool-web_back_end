const hasValuesFromArray = (set, array) => {
  const isBelowThreshold = (currentValue) => set.has(currentValue);

  return array.every(isBelowThreshold);
};

export default hasValuesFromArray;
