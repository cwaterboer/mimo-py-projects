todo_list=[]

while True:
  if not todo_list:
    print('Your ToDo list is empty')

  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index+=1

  print('Options:')
  print('1) Add Task')
  print('2) Remove Task')
  print('3) Quit')

  choice = input('Which one do you choose 1, 2, 3?')
  
  if choice == '1':
    print('Adding new task')
    new_task = input("Enter the task: ")
    todo_list.append(new_task)
    print(f"Task '{new_task}' added to the ToDo list")
  elif choice == '2':
    print('Removing task')
    if len(todo_list)>0:
      removed_task = todo_list.pop()
    else:
      print("ToDo List is empty")
      
  elif choice == '3':
    print('Quitting')
    break
  
