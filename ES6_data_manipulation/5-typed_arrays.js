export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const vi = new DataView(buffer);

  if (position < length) {
    vi.setInt8(position, value);
  } else {
    throw Error('Position outside range');
  }
  return vi;
}
