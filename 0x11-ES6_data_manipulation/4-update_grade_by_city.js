const updateStudentGradeByCity = (a, c, nG) => a
  .filter((it) => it.location === c)
  .map((itm) => {
    const newItem = { ...itm };

    const student = nG.find((it) => it.studentId === itm.id);
    if (student) newItem.grade = student.grade;
    else newItem.grade = 'N/A';
    return newItem;
  });

export default updateStudentGradeByCity;
