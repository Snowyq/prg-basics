
file_name = 'it_company.csv'

try: 
    with open(file_name, 'r') as file:
        content = file.read()
        file_lines = content.splitlines()
        counter = 0
    while True:
        input('press Enter...')
        for i in range(counter, counter + 5):
            print(file_lines[i])
        counter += 5
except:
    print('error')