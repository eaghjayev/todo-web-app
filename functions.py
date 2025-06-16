FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
     to-do items.
     """
    with open(filepath, "r") as data_file:
        return data_file.readlines()


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list to a text file."""
    with open(filepath, "w") as data_file:
        data_file.writelines(todos_arg)

print("Hello from functions")