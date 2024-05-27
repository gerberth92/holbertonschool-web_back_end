export default function getStudentsByLocation(lista, city) {
  const result = lista.filter((obj) => obj.location === city);

  return result;
}
