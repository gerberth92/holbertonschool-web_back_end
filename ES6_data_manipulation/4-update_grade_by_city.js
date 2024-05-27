export default function updateStudentGradeByCity(lista, city, newGrades) {
  return lista
    .filter((obj) => obj.location === city)
    .map((std) => {
      const data = newGrades.find((item) => item.studentId === std.id);

      return {
        ...std,
        grade: data ? data.grade : 'N/A',
      };
    });
}
