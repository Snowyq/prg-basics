with open('it_company.csv', 'r') as file:
  content = file.read()
  file_lines = content.splitlines()
  query_position = 'Software Engineer'
  searched_employees = []

  
  for employee in file_lines:
    employee_desc = employee.split(',')
    if employee_desc[2] == query_position:
      searched_employees.append(f'{len(searched_employees) + 1}. {employee}')

  print(searched_employees)
