export default function getListStudentIds(lista) {
  if (lista instanceof Array) {
    return lista.map((obj) => obj.id);
  }
  return [];
}
