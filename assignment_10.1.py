import os
user_path = ""
def save_file():
    global user_path
    if user_path == "":
        user_path = input("Enter save location: ")
    isdir = os.path.exists(user_path)
    if isdir == True:
        user_path = user_path + "\\"
        user_file = user_path + input("Enter file name: ") + ".txt"
        isFile = os.path.isfile(user_file)
        if isFile == True:
            response = input("Overwrite existing file? 'yes' or 'no': ")
            if response == "no" or response == "n":
                print("Please enter a new file name.")
                save_file()
            else:
                print("File overwritten.")
        with open(user_file, 'w+') as file_object:
            file_object.write(input("Please enter your name: "))
            file_object.write(", ")
            file_object.write(input("Please enter your address: "))
            file_object.write(", ")
            file_object.write(input("Please enter your phone number: "))
        print("Data saved!")
        with open(user_file) as file_object:
            contents = file_object.read()
        print(contents)
    else:
        print("That directory was not found, please try again.")
        save_file()
save_file()