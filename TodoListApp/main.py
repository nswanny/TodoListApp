while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task to add: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()

            todos.append(todo)
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case 'edit':
            number = int(input("Which task would you like to edit? (Enter the number.): ")) 
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo that is complete: "))
            todos.pop(number - 1)
        case 'exit':
            break

print("Goodbye!")