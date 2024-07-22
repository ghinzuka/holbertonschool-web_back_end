export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentCity = students.filter((student) => student.location === city);
  return studentCity.map((student) => {
    const matchingGrade = newGrades
      .filter((grade) => grade.studentId === student.id)
      .map((grade) => grade.grade)[0];

    return {
      ...student,
      grade: matchingGrade !== undefined ? matchingGrade : 'N/A',
    };
  });
}
