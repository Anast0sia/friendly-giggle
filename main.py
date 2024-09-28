HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

today = []
tomorrow = []
other = []
tasks = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    data = input("Введите дату: ")
    if data == "Сегодня":
      today.append(data)
    elif data == "Завтра":
      tomorrow.append(data)
    else:
      other.append(data)
    task = input("Введите название задачи: ")
    tasks.append(task)
    print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование! ")
    break
  else:
    print("Неизвестная команда! ")
    break

print("До свидания!")
