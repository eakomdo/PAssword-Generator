#A to-do list application with user authentication and role-based access control

from getpass import getpass
from datetime import datetime

accounts = {}

# This code implements a simple to-do list application with user authentication and role-based access control.
def sign_up():
    print("Sign-Up: Create a new account.")
    username = input("Enter a username: ").strip()
    if username in accounts:
        print("Username already exists. Please try again.")
        return sign_up()
    password = getpass("Enter a password: ").strip()
    role = input("Enter your role (admin/user): ").strip().lower()
    if role not in ["admin", "user"]:
        print("Invalid role. Please enter 'admin' or 'user'.")
        return sign_up()
    accounts[username] = {"password": password, "role": role, "todo_list": []}
    print(f"Account created successfully! You can now log in as {role}.")
    
    # Redirect to login or dashboard based on role
    if role == "admin":
        admin_login()
    elif role == "user":
        user_login()
        

# This code implements a to-do list application with user authentication and role-based access control.
def admin_login():
    print("Admin Login:")
    username = input("Enter your username: ").strip()
    password = getpass("Enter your password: ").strip()
    if username in accounts and accounts[username]["role"] == "admin" and accounts[username]["password"] == password:
        print(f"Login successful! Welcome, {username}.")
        admin_dashboard()
    else:
        print("Login failed. Please check your username and password.")
        admin_login()
        

# This code implements admin login functionality for the to-do list application.
def admin_dashboard():
    print("Admin Dashboard:")
    print("1. View all user dashboards")
    print("2. Assign permissions to users")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        for user, data in accounts.items():
            if data["role"] == "user":
                print(f"{user}'s To-Do List:")
                for task, time in data["todo_list"]:
                    print(f"- {task} (Added on: {time})")
    elif choice == "2":
        user = input("Enter the username to assign permissions: ").strip()
        if user in accounts and accounts[user]["role"] == "user":
            permission = input("Enter the permission to assign: ").strip()
            accounts[user].setdefault("permissions", []).append(permission)
            print(f"Permission '{permission}' assigned to {user}.")
        else:
            print("Invalid username or not a user.")
    else:
        print("Invalid choice.")
        
        
# This code allows an admin to view all user dashboards and assign permissions to users.
def user_login():
    print("User Login:")
    username = input("Enter your username: ").strip()
    password = getpass("Enter your password: ").strip()
    if username in accounts and accounts[username]["role"] == "user" and accounts[username]["password"] == password:
        print(f"Login successful! Welcome, {username}.")
        user_dashboard(username)
    else:
        print("Login failed. Please check your username and password.")
        user_login()
        
        
# This code implements user login functionality for users in the to-do list application.
def user_dashboard(username):
    print("User Dashboard:")
    todo_list = accounts[username]["todo_list"]
    while True:
        print("1. Add a task")
        print("2. View tasks")
        print("3. Logout")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            task = input("Enter a task: ").strip()
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            todo_list.append((task, time))
            print(f"Task '{task}' added at {time}.")
        elif choice == "2":
            print("Your To-Do List:")
            print("================================================")
            for task, time in todo_list:
                print(f"- {task} (Added on: {time})")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
            continue

# This code implements a user dashboard for managing tasks in the to-do list application.
def main():
    print("Welcome to the system!")
    print("1. Sign Up")
    print("2. Log In")
    choice = input("Enter your choice: ").strip()
    
    while True:
        if choice == "1":
            sign_up()
            break  # Exit the loop after successful sign-up
        elif choice == "2":
            role = input("Are you an admin or a user? (admin/user): ").strip().lower()
            if role == "admin":
                admin_login()
                break  # Exit the loop after successful login
            elif role == "user":
                user_login()
                break  # Exit the loop after successful login
            else:
                print("Invalid role. Please enter 'admin' or 'user'.")
        else:
            print("Invalid choice. Please enter '1' for Sign Up or '2' for Log In.")
            choice = input("Enter your choice: ").strip()  # Prompt the user again
            

if __name__ == "__main__":
    main()