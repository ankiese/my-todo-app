#from functions import get_todos, write_todos" and list all of the functions available.
FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH): #add the default value for the parameter to not have it later.
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
# print(help(get_todos) for anyone that wants to see what the title says.

def write_todos(todos_arg, filepath=FILEPATH): #todos_arg is not a default parameter because we are always changing the list. Change the order.. nondefaults, then default.
    """ Write a to-do items list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

# print(__name__)

if __name__ == "__main__": #"name is the name of the variable functions or main if its in this page")
    print("Hello")
    print(get_todo())