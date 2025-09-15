print ("Welcome to to-do app")
action = input("What do you want to do? (add, edit, show, exit): ")



while action != "exit":
    if action == "add":
        item = input("What do you want to add? ")
    elif action == "edit":
        delete = input("What do you want to delete? ")
    elif action == "show":
        print(display)
             
