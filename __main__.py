import os
import glob
from pathlib import Path


class TodoList:

    def __init__(self, name_lowercase):
        self.name = name_lowercase
        try:
            """
            Creates a directory for todo items
            and a subdirectory for completed items.
            """
            os.mkdir("logs\\" + name_lowercase)
            os.mkdir("logs\\" + name_lowercase + "\\completed\\")
        except FileExistsError:
            print(f"Welcome back {user_name}!\n")
        except (OSError, FileNotFoundError):
            print("Impossible username\n")
        """
        Changing working directory to the newly created directory.
        """
        os.chdir("logs\\" + name_lowercase)


def menu():
    menu_choice = input("\nMenu:\n"
                        "[1]\tView todo list\n"
                        "[2]\tAdd new item\n"
                        "[3]\tComplete item\n"
                        "[4]\tDelete item\n"
                        "[5]\tView completed items\n"
                        "[0]\tExit\n"
                        "Select number:\t")
    print()
    selection(menu_choice)


def view_todos():
    print(f"\n{str(user_name)}'s To-Do List.\n")
    todo_list = glob.glob(f"{path}\\*.txt")
    counter = 1      
    if todo_list:
        for todo in todo_list:
            if "completed" in todo:
                continue
            else:
                print(f"{counter}:\t{todo[len(path) + 1:-4]}")
                counter += 1
    else:
        print("No items in list")
    print()


def add_item():
    task = input("Enter name of todo item:\n")
    print()
    task_description = input(
        "Add a description if you like (press Enter to continue)\n")
    print()
    try:
        if task:
            new_file = open(f"{path}\\{task}.txt", "w+")
            new_file.write(f"{task}\n{task_description}")
            print(f"{task} added to {user_name}'s To-Do List")
        elif task.isspace():
            print("You did not enter a name for the item")
        else:
            print("You did not enter a name for the item")
    except OSError:
        print("Impossible name for item")


def complete_item():
    completed_item = input("What is the name of the item you have completed?\n")
    try:
        if completed_item:
            Path(f"{path}\\{completed_item}.txt") \
                .rename(f"{path}\\completed\\{completed_item}.txt")
            print(f"\n{completed_item} was completed. Well done!")
        else:
            print("You did not enter a name for the item")
    except PermissionError:
        print(f"You cannot complete {completed_item} in this session")
    except FileNotFoundError:
        print("You can only complete items from your To Do List")


def delete_item():
    item_to_delete = input("What is the name of the item you wish to delete?\n")
    if os.path.exists(f"{path}\\{item_to_delete}.txt"):
        os.remove(f"{path}\\{item_to_delete}.txt")
        print()
        print(f"{item_to_delete} has been deleted.")
    elif os.path.exists(f"{path}\\completed\\{item_to_delete}.txt"):
        os.remove(f"{path}\\completed\\{item_to_delete}.txt")
        print()
        print(f"{item_to_delete} has been deleted.")
    else:
        print("File does not exist")


def view_completed():
    print(f"{str(user_name)}'s completed items.\n")
    completed_list = glob.glob(f"{path}\\completed\\*.txt")
    counter = 0
    if completed_list:

        for item in completed_list:
            print(f"{counter + 1}:\t" + item[len(f"{path}\\completed\\"): -4])
            counter += 1
    else:
        print("No completed items yet :(")


def selection(choice):
    if choice == "1":
        view_todos()
    elif choice == "2":
        add_item()
    elif choice == "3":
        complete_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        view_completed()
    elif choice == "0":
        exit()
    else:
        print("The option that you selected was not available.")


user_name = input("Enter username:\n")
TodoList(user_name.casefold())
path = os.getcwd()
while True:
    menu()
