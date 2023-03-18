import os

def print_tree(path, prefix=''):
    """Prints the file tree for a specified folder."""
    files = os.listdir(path)
    files = sorted(files, key=lambda s: s.lower())
    for index, item in enumerate(files):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item.endswith('.py'):
            if index == len(files) - 1:
                print(f"{prefix}└── {item}")
            else:
                print(f"{prefix}├── {item}")
        elif os.path.isdir(item_path) and item not in ['venv','.git','__pycache__']:
            if index == len(files) - 1:
                print(f"{prefix}└── {item}/")
                print_tree(item_path, prefix=prefix+'    ')
            else:
                print(f"{prefix}├── {item}/")
                print_tree(item_path, prefix=prefix+'│   ')

# Get the current parent directory of the running Python script
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# Call `print_tree` function, but only print `.py` files
print(f"{os.path.basename(parent_dir)}/")
print_tree(parent_dir, prefix='')

