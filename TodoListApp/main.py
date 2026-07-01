todos = []

while True:
    user_action = input("Type 'add', 'show', 'edit' or 'exit': ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task to add: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Which task would you like to edit? (Enter the number.): ")) 
            existing_todo = todos[number]
        case 'exit':
            break

print("Goodbye!")