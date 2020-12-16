import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignup = async (
  firstName = '',
  lastName = '',
  fileName = '',
) => {
  const data = await Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((data) => {
    const newData = data.map((val) => {
      const newVal = val;
      if (val && val.reason) {
        newVal.value = val.reason.toString();
        delete newVal.reason;
      }
      return newVal;
    });
    return newData;
  });
  return data;
};

export default handleProfileSignup;
