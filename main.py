dict = {}
for i in range(0, 3):
  data = input("Введите дату: ")
  task = input("Введите задачу: ")
  dict[data] = task
for i in dict.keys():
  print(f'{i} {dict[i]}')