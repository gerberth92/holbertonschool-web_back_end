export default function createEmployeesObject(departmentName, employees) {
  const dic = {};
  dic[departmentName] = employees;

  return dic;
}
