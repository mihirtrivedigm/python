import os

def change_name(filename):
    start = filename.find('P')
    end = filename.find('.')
    if start != -1 and end != -1:
        result3 = filename[start:end]
    print result3
    filename = filename.replace(result3,"")
    result4 = result3 + " " + filename
    return result4

def file_program():
    list_of_files = os.listdir(r"D:\coding venture\Python\udacity\AI")
    saved_path = os.getcwd()
    print("Current working directory is: "+saved_path)
    os.chdir(r"D:\coding venture\Python\udacity\AI")
    #print "Old file name: ",list_of_files
    #print("Old names: " + os.listdir(r"D:\Mihir Study\white panda"))
    for file_name in list_of_files:
        print "Old file name: ", file_name
        a = change_name(file_name)
        #os.rename(file_name, a)
        os.rename(file_name,a)
        print "New file name: ",a
        #print "New file name: ", file_name.translate(None, "Mod-01 ")
    os.chdir(r"D:\coding venture\Python\udacity\AI")
    #print("New names: " + os.listdir(r"D:\Mihir Study\white panda"))


file_program()
