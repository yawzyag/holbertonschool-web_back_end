const getStudentIdsSum = (a) => a.reduce((acc, itm) => acc + itm.id, 0);

export default getStudentIdsSum;
