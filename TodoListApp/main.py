while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task to add: ") + "\n"

            with  open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")

        case 'edit':
            number = int(input("Which task would you like to edit? (Enter the number.): ")) 
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            
            todos[number] = new_todo + '\n'
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo that is complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

print("Goodbye!")