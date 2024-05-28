export default function updateUniqueItems(ma) {
  if (ma instanceof Map) {
    for (const [clave, valor] of ma.entries()) {
      if (valor === 1) {
        ma.set(clave, 100);
      }
    }
  } else {
    throw Error('Cannot process');
  }
  return ma;
}
