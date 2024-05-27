export default function getStudentIdsSum(lista) {
  const suma = lista.reduce((a, b) => a + b.id, 0);

  return suma;
}
