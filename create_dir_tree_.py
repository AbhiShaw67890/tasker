import os

def generate_tree(directory, indent=''):
    items = os.listdir(directory)
    for i, item in enumerate(sorted(items)):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            if i == len(items) - 1:
                print(indent + '└── ' + item + '/')
                generate_tree(path, indent + '    ')
            else:
                print(indent + '├── ' + item + '/')
                generate_tree(path, indent + '│   ')
        else:
            if i == len(items) - 1:
                print(indent + '└── ' + item)
            else:
                print(indent + '├── ' + item)

# Get the current directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Generate the tree-like structure
generate_tree(current_directory)
