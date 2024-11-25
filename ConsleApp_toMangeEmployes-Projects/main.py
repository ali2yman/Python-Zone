import auth
import projects

def pro(email):
    if email:  
        logged_in_user = email
        while True:
            print("---- Project Management ----")
            print("1 - Create Project")
            print("2 - View Projects")
            print("3 - Edit My Project")
            print("4 - Delete My Project")
            print("5 - Logout")

            project_choice = input("Enter your choice: ")

            if project_choice == "1":
                projects.create_project(logged_in_user)
            elif project_choice == "2":
                projects.view_projects()
            elif project_choice == "3":
                projects.edit_project(logged_in_user)
            elif project_choice == "4":
                projects.delete_project(logged_in_user)
            elif project_choice == "5":
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice.")
    else:
        print("Login failed. Returning to main menu.")


def main():
    """Main Menu for User Management."""
    while True:
        print("\n------ Crowd-Funding Console App -------")
        print("1 - Register User")
        print("2 - Login User")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            auth.register_user()
        elif choice == "2":
            email = auth.login_user()
            if email:  
                print(f"Welcome, {email}!")
                pro(email)
            else:
                print("Login failed. Please try again.")
        elif choice == "3":
            print("M3a alf Salama")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
