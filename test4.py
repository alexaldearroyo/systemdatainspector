import subprocess
import os

def get_size(path):
    try:
        expanded_path = os.path.expanduser(path)
        result = subprocess.run(['sudo', 'du', '-shx', expanded_path], capture_output=True, text=True, check=True)
        size_str = result.stdout.split()[0]
        size_num, size_unit = float(size_str[:-1]), size_str[-1]
        
        if size_unit == 'B':
            size_in_bytes = size_num * 1
        elif size_unit == 'K':
            size_in_bytes = size_num * 1024
        elif size_unit == 'M':
            size_in_bytes = size_num * 1024 ** 2
        elif size_unit == 'G':
            size_in_bytes = size_num * 1024 ** 3
        else:
            size_in_bytes = size_num
        
        return size_in_bytes
    except subprocess.CalledProcessError as e:
        return -1  # Devuelve un valor negativo en caso de error

def format_size(size_bytes):
    try:
        if size_bytes < 0:  # Comprueba si el tamaño es negativo
            return "Unknown size, insufficient permissions)"  # Devuelve un mensaje apropiado
        
        size_kb = size_bytes / 1024
        size_mb = size_bytes / (1024 ** 2)
        size_gb = size_bytes / (1024 ** 3)
        
        if size_bytes < 1024 * 1024:
            return f"\033[1;32m{size_kb:.2f}\033[0m KB"  # Green text for KB
        elif size_bytes < 1024 * 1024 * 1024:
            return f"\033[1;33m{size_mb:.2f}\033[0m MB"  # Orange text for MB
        else:
            return f"\033[1;31m{size_gb:.2f}\033[0m GB"  # Red text for GB
    except TypeError as e:
        return f"Error formatting the size: {e}"

def list_subdirectories_and_files(parent_dir):
    subdirs_and_files = [item for item in os.listdir(parent_dir) if os.path.exists(os.path.join(parent_dir, item))]
    return subdirs_and_files if subdirs_and_files else None

def ask_yes_no_question(question):
    while True:
        response = input(f"{question} (y/n): ").lower()
        if response in ["y", "yes", "n", "no"]:
            return response
        print("Invalid input. Please enter 'y' or 'n'.")

def get_valid_user_response():
    while True:
        user_response = input("Do you want to inspect the directories? (y/n): ").lower()
        if user_response in ["y", "yes", "n", "no"]:
            return user_response
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

directories = [
    "~/Library/Caches/",
    "/tmp/",
    "/var/tmp/",
    "/private/var/vm/",
    "/Library/Updates/",
    "/Library/Application Support/",
    "~/Library/Application Support/",
    "/var/log/",
    "~/Library/Logs/",
    "/Library/Preferences/",
    "~/Library/Preferences/"
]

def display_directories_with_sizes(first_display=True):
    if not first_display:
        print("\033[1;37;104mSystem Data Directories\033[0m\n")  # Blue background text only for subsequent displays
    for directory in directories:
        size = get_size(directory)
        formatted_size = format_size(size)
        print(f"The size of {directory} is: {formatted_size}")

print("\n\033[1;33mMACOS SYSTEM DATA INSPECTOR\033[0m\n")  # Yellow text
print("\033[1;37;104mApproximate calculation of the potentially modifiable space occupied by System Data on your Mac\033[0m\n")

display_directories_with_sizes()

print()  # Create a newline
separator = '=' * 60  # Yellow graphical separator
print("\033[1;33m" + separator + "\033[0m")  # Yellow separator

while True:
    user_response = ask_yes_no_question("Do you want to inspect any directory?")

    if user_response in ["n", "no"]:
        break

    directory_to_inspect = input("\033[1;32mPlease specify the directory you want to inspect:\033[0m ")
    print("\033[1;37;104mLet's proceed with the inspection of the directory\033[0m\n")

    dir_size = get_size(directory_to_inspect)
    formatted_dir_size = format_size(dir_size)
    print(f"{directory_to_inspect} ({formatted_dir_size})")

    subdirs_and_files = list_subdirectories_and_files(os.path.expanduser(directory_to_inspect))
    if subdirs_and_files:
        print("\033[1;33m" + separator + "\033[0m")  # Yellow separator
        for item in subdirs_and_files:
            item_path = os.path.join(os.path.expanduser(directory_to_inspect), item)
            item_size = get_size(item_path)
            formatted_item_size = format_size(item_size)
            print(f"{item} ({formatted_item_size})")

        # Ask to open the directory in Finder
        open_in_finder = ask_yes_no_question(f"Do you want to open {directory_to_inspect} in Finder?")
        if open_in_finder in ["y", "yes"]:
            subprocess.run(["open", os.path.expanduser(directory_to_inspect)])
    
    print("\n\033[1;37;104mEnd of the inspection\033[0m\n")
    display_directories_with_sizes(first_display=False)  # We make sure it's no longer the first display.

print("\n\033[1;37;104mInspection finished\033[0m\n")
print("Thank you for using MacOS System Data Inspector, by Alex Arroyo\n")
