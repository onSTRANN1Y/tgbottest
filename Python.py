# Пример записи в файл
with open('example.txt', 'w') as file:
    file.write('Привет, мир!\nЭто пример записи в файл.')

# Пример чтения из файла
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)