const weakMap = new WeakMap();
const queryAPI = (endpoint) => {
  let count = weakMap.get(endpoint) || 0;
  if (count >= 5) throw new Error('Endpoint load is high');
  weakMap.set(endpoint, (count += 1));
};

export { weakMap, queryAPI };
