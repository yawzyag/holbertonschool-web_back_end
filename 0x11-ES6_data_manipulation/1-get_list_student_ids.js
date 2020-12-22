const checkArr = (arr) => arr && Array.isArray(arr);
const getListStudentIds = (listObj) => (checkArr(listObj) ? listObj.map((item) => item.id) : []);
export default getListStudentIds;
