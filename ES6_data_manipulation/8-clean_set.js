export default function cleanSet(set, startString) {
  const li = [];

  if (!startString) {
    return '';
  }

  for (const v of set) {
    if (v.startsWith(startString)) {
      li.push(v.slice(startString.length));
    }
  }
  return li.join('-');
}
