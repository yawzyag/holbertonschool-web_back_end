const updateUniqueItems = (mapArg) => {
  if (!(mapArg instanceof Map)) throw new Error('Cannot process');

  mapArg.forEach((val, key) => {
    if (val === 1) mapArg.set(key, 100);
  });
};

export default updateUniqueItems;
