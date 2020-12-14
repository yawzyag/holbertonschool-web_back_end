import { createUser, uploadPhoto } from './utils';

const asyncUploadUser = async () => {
  let data = {
    photo: null,
    user: null,
  };
  try {
    data = {
      photo: await uploadPhoto(),
      user: await createUser(),
    };
    return data;
  } catch (error) {
    return data;
  }
};

export default asyncUploadUser;
