import os

def file_program():
    list_of_files = os.listdir(r"D:\Mihir Study\white panda")
    saved_path = os.getcwd()
    print("Current working directory is: "+saved_path)
    os.chdir(r"D:\Mihir Study\white panda")
    print(list_of_files)
    for file_name in list_of_files:
        a = file_name.translate(None, "0123456789")
        os.rename(file_name, a)
    os.chdir(r"D:\Mihir Study\white panda")


file_program()
