import subprocess

import pyautogui
import time


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




    # OPEN GIT BASH
    # Option 1: open with Popen with an assumed directly path 
    # Path to the Git Bash executable
    # git_bash_path = r"C:\Program Files\Git\git-bash.exe"

    # # Use subprocess.Popen to open Git Bash
    # subprocess.Popen(git_bash_path)

    # Option 2: use windows search to launch it
    time.sleep(2)
    pyautogui.press('win')

    time.sleep(1)
    pyautogui.typewrite('git bash')

    time.sleep(1)
    pyautogui.press('enter')

    # ADD CHECKER TO MAKE SURE BASH WINDOW IS STILL OPEN BEFORE CONTINUING?


    # NAVIGATE TO CODING FOLDER
    time.sleep(2)
    if folder_path == "coding":
        pyautogui.typewrite("cd documents/coding")

    if folder_path == "frontendmentor":
        pyautogui.typewrite("cd documents/coding/frontendmentor")

    time.sleep(0.3)
    pyautogui.press('enter')

    # NAVIGATE TO PROJECT FOLDER
    pyautogui.typewrite(f"cd {project_name}")
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(1)



    # RUN CRA W/ TYPESCRIPT
    project_directory = ""

    command = ["npx create-react-app app --template typescript"]
    subprocess.run(command, shell=True, check=True, cwd=project_directory, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)





create_cra()