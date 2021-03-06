function handleResponseFromAPI(promise) {
  const obj = { status: 200, body: 'success' };
  return promise
    .then(() => obj)
    .catch((e) => e)
    .finally(() => console.log('Got a response from the API'));
}

export default handleResponseFromAPI;
