'''
Task 17 'Task Management System' application that based on user choice, 
lists from two text files all and user specific tasks, adds new task and 
outputs 'generated' reports as two text files.
Code Author: Bharat Penumathsa
Id: BP23010007956

'''

# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========

import os
from datetime import datetime, date

# Defining a function to register a new user and write to text file user.txt
def reg_user():
    '''Add a new user to the user.txt file'''
    print("\nAdding a New User")
    print("-------------------")
    new_username = input("\nNew Username: ")

    while new_username in username_password:
        print("Sorry! Username already exists. Please enter a different username.")
        new_username = input("New Username: ")

    new_password = input("New Password: ")
    confirm_password = input("Confirm Password: ")

    if new_password == confirm_password:
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))
    else:
        print("Passwords do not match")

# Defining a function to add new task and write to the text file task.txt
def add_task():
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    print("\nAdding a New Task")
    print("---------------------")
    task_username = input("\nName of person assigned to task: ")
    if task_username not in username_password.keys():
        print("\nUser does not exist. Please enter a valid username")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        task_due_date = input("Due date of task (YYYY-MM-DD): ")
        try:
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT).date()
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    
    # Then get the current date.
    curr_date = date.today()

    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

    print("Task successfully added.")

# Defining a function to view all tasks printed to console by reading from task.txt file
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling)         
    '''
    print('\n You are viewing all tasks: \n')
    print('\n----------------------------------\n')
    for i, t in enumerate(task_list, start=1):
        disp_str = f"Task {i}:\n"
        disp_str += f"Title: {t['title']}\n"
        disp_str += f"Assigned to: {t['username']}\n"
        disp_str += f"Date Assigned: {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description:\n{t['description']}\n"
        disp_str += f"Completed: {'Yes' if t['completed'] else 'No'}\n"
        print(disp_str)
        print('\n----------------------------------\n')

# Defining a function to view user specific task printed to console by reading from task.txt file
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling)
    '''
    print('\n----------------------------------\n')
    j_ierator = 1 #iterator to start the task numbering starting from '1'
    for i, t in enumerate(task_list, start=1):
        if t['username'] == curr_user:
            disp_str = f"Task {j_ierator}:\n"
            disp_str += f"Title: {t['title']}\n"
            disp_str += f"Assigned to: {t['username']}\n"
            disp_str += f"Date Assigned: {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description:\n{t['description']}\n"
            disp_str += f"Completed: {'Yes' if t['completed'] else 'No'}\n"
            print(disp_str)
            j_ierator += 1
    print('-------------------------------------')

    task_choice = input("\nEnter the task number to edit or mark as complete, or enter '-1' to return to the main menu: ")

    if task_choice == '-1':
        return
    else:
        task_choice = int(task_choice) - 1
        if 0 <= task_choice < len(task_list):
            task = task_list[task_choice]
            print("\nChoose from the following:")
            print("1. Mark the task as complete")
            print("2. Edit the task")
            choice = input("Enter your choice: ")

            if choice == '1':
                task['completed'] = True
                print("Task marked as complete.")
            elif choice == '2':
                task['title'] = input("Please enter a new title: ")
                task['description'] = input("Please enter a new description: ")
                new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                try:
                    due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT).date()
                    task['due_date'] = due_date_time
                    print("Task has been updated successfully.")
                except ValueError:
                    print("Sorry! Invalid datetime format. Task not updated.")
            else:
                print("Sorry! Invalid choice. Task not updated.")
        else:
            print("Invalid task number. Please try again.")

# Defining a function to generate reports related to tasks and write the details 
# to a text file 'task_overview.txt'.
def generate_reports():
    with open("task_overview.txt", "w") as file_overview:
        total_tasks = len(task_list)
        completed_tasks = sum(task["completed"] for task in task_list)
        uncompleted_tasks = total_tasks - completed_tasks
        
        present_day = date.today()
        overdue_tasks = sum(1 for t in task_list if not t["completed"] and t["due_date"] < present_day)

        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
        overdue_percentage = (overdue_tasks / total_tasks) * 100

        file_overview.write("Task Overview\n\n")
        file_overview.write("Total number of tasks generated and tracked: {}\n".format(total_tasks))
        file_overview.write("Total number of combined tasks: {}\n".format(total_tasks))
        file_overview.write("Total number of uncompleted tasks: {}\n".format(uncompleted_tasks))
        file_overview.write("Total number of tasks that haven't been completed and are overdue: {}\n".format(overdue_tasks))
        file_overview.write("Percentage of tasks that are incomplete: {:.2f}%\n".format(incomplete_percentage))
        file_overview.write("Percentage of tasks that are overdue: {:.2f}%\n".format(overdue_percentage))
        

    with open("user_overview.txt", "w") as user_file_overview:
        total_users = len(username_password)
        user_file_overview.write("User Overview\n\n")

        for user in username_password.keys():
            user_tasks = [task for task in task_list if task["username"] == user]
            total_user_tasks = len(user_tasks)
            user_completed_tasks = sum(task["completed"] for task in user_tasks)
            user_uncompleted_tasks = total_user_tasks - user_completed_tasks
            user_overdue_tasks = sum(1 for t in user_tasks if not t["completed"] and t["due_date"] < present_day)
            
            if total_tasks > 0 and total_user_tasks > 0:
                user_task_percentage = (total_user_tasks / total_tasks) * 100
                user_completed_percentage = (user_completed_tasks / total_user_tasks) * 100
                user_uncompleted_percentage = (user_uncompleted_tasks / total_user_tasks) * 100
                user_overdue_percentage = (user_overdue_tasks / total_user_tasks) * 100
            else:
                print("\nNo tasks are allocated")

            user_file_overview.write(f"User: {user}\n")
            user_file_overview.write("Total number of users registered: {}\n".format(total_users))
            user_file_overview.write("Total number of tasks generated and tracked: {}\n".format(total_tasks))
            user_file_overview.write(f"Total number of tasks assigned to the user: {total_user_tasks}\n")
            user_file_overview.write(f"Percentage of the total number of tasks assigned to the user: {user_task_percentage:.2f}%\n")
            user_file_overview.write(f"Percentage of the total number of tasks assigned to the user that have been completed: {user_completed_percentage:.2f}%\n")
            user_file_overview.write(f"Percentage of the total number of tasks assigned to the user that must still be completed: {user_uncompleted_percentage:.2f}%\n")
            user_file_overview.write(f"Percentage of the total number of tasks assigned to the user that have not yet been completed and are overdue: {user_overdue_percentage:.2f}%\n")

    print("\nTask and User overview reports generated successfully.")


# Defining a function that displays stats to the admin user 
def display_stats():
    '''If the user is an admin they can display statistics about number of users
       and tasks.'''
    if curr_user == 'admin':
        num_users = len(username_password)
        num_tasks = len(task_list)
        print('\nDisplaying statistics\n')
        print("-----------------------------------")
        print(f"Number of users: {num_users}")
        print(f"Number of tasks: {num_tasks}")
        print("-----------------------------------")

        # Displaying task overview
        with open("task_overview.txt", "r") as task_overview_file:
            task_overview = task_overview_file.read()
            print('-----------------------------------')
            print(task_overview)
            print('-----------------------------------')

        # Displaying user overview
        with open("user_overview.txt", "r") as user_overview_file:
            user_overview = user_overview_file.read()
            print('-----------------------------------')
            print(user_overview)
            print('-----------------------------------')

# Defining date variable
DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file: #
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT).date()
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT).date()
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    task_list.append(curr_t)

# ====Login Section====

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
curr_user = ""

while not logged_in:
    print("\nLOGIN")
    print("----------------------")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
    else:
        print("Login Successful!")
        logged_in = True


# Main menu for Task Management System (TMS)
while True:
    print()
    menu = input('''Select one of the following options:

    r - Register a user
    a - Add a task
    va - View all tasks
    vm - View my tasks
    gr - Generate reports
    ds - Display statistics
    e - Exit

    : ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_reports()

    elif menu == 'ds':
        if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
            generate_reports()
        display_stats()

    elif menu == 'e':
        break

    else:
        print("\nInvalid option. Please try again.")
