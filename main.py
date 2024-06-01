import function


while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = function.get_todos()
        todos.append(todo + "\n")
        function.write_todos(todos)
        print(todos)

    elif user_action.startswith("show"):
        todos = function.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1} - {item}")

    elif user_action.startswith("edit"):
        try:
            new_todo = input("Type New Todo: ")
            number_to_edit = int(user_action[5:]) - 1
            todos = function.get_todos()
            todos[number_to_edit] = new_todo + "\n"
            function.write_todos(todos)
            print(todos)
        except IndexError:
            print("Command Invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            number_to_complete = int(user_action[9:]) - 1
            todos = function.get_todos()
            todos_to_remove = todos[number_to_complete].strip("\n")
            todos.pop(number_to_complete)
            function.write_todos(todos)
            print(f"{todos_to_remove} was removed from the list")
        except IndexError:
            print("Command Invalid")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command Invalid")