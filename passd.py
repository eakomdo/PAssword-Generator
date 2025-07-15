from getpass import getpass

def admin_login():
    print("Welcome to the admin login system.")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "admin" and password == "secret":
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Login failed. Please check your username and password.")
        admin_login()


def user_login():
    print("Welcome to the user login system.")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "user" and password == "password":
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Login failed. Please check your username and password.")
        
        
def main():
    print ("Welcome to the login system.")
    choice = input("Are you an admin or a user? (admin/user): ").strip().lower()
    if choice == "admin":
        admin_login()
    elif choice == "user":
        user_login()  # Call the user_login function for the "user" choice
    else:
        print("Invalid choice. Please enter 'admin' or 'user'.")
        main()
    
    #create a to do list for the user
    todo_list = []
    while True:
        task = input("Enter a task to add to your to-do list (or type 'done' to finish): ")
        if task.lower() == 'done':
            break
        todo_list.append(task)
    print("Your to-do list:")
    for item in todo_list:
        print(f"- {item}")

main()
admin_login()
user_login()