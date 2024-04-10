import subprocess


def create_cra():

    # # GET INFO FROM USER
    # Prompt the user for the folder path where the project will be created
    folder_path = input("Please enter the folder path where the project will be created: ")

    # Exit program if folder is invalid
    if folder_path != "coding" and folder_path != "frontendmentor":
        print("invalid input")
        return

    # Prompt the user for the name of the project folder
    project_name = input("Please enter the name of the project folder: ")

    # Just for demonstration, print out the collected information
    print(f"Folder Path: {folder_path}")
    print(f"Project Name: {project_name}")




    # # OPEN GIT BASH
    # # Path to the Git Bash executable
    # git_bash_path = r"C:\Program Files\Git\git-bash.exe"

    # # Use subprocess.Popen to open Git Bash
    # subprocess.Popen(git_bash_path)

    # # ADD CHECKER TO MAKE SURE BASH WINDOW IS STILL OPEN BEFORE CONTINUING?


create_cra()