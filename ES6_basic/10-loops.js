export default function appendToEachArrayValue(array, appendString) {
  const news = [...array];

  for (const value of news) {
    const idx = array.indexOf(value);
    news[idx] = appendString + value;
  }

  return news;
}
