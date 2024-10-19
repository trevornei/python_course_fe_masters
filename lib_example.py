import os
# imports operating system functions.

my_folder = os.getcwd()
print(f"Get files in: {my_folder}")

# Use context manager to clean up files.
with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f"Name of entery: {entry.name}")