print ("Welcome to to-do app")
action = input("What do you want to do? (add, edit, show, exit): ")



while action != "exit":
    if action == "add":
        todo = input("Enter a to-do item: ")
        with open("todos.txt", "a") as file:
            file.write(todo + "\n")
        print(f'Added to-do: "{todo}"')

    elif action == "show":
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        print("Your to-do list:")
        for index, item in enumerate(todos, start=1):
            print(f"{index}. {item.strip()}")

    elif action == "edit":
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        print("Your to-do list:")
        for index, item in enumerate(todos, start=1):
            print(f"{index}. {item.strip()}")
        try:
            item_number = int(input("Enter the number of the item you want to edit: "))
            if 1 <= item_number <= len(todos):
                new_todo = input("Enter the new to-do item: ")
                todos[item_number - 1] = new_todo + "\n"
                with open("todos.txt", "w") as file:
                    file.writelines(todos)
                print(f'Updated item {item_number} to "{new_todo}"')
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Invalid action. Please choose from (add, edit, show, exit).")

    action = input("What do you want to do? (add, edit, show, exit): ")
    
