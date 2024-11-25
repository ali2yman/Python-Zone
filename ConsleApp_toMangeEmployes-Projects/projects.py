import json
import re



def load_projects(file_name="projects.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []                                 #  Return an empty list if the file is missing or corrupted
    except Exception as e:
        print(e)
        return []

def save_data(data,file_name="projects.json"):
    with open(file_name,"w") as file:
        json.dump(data,file,indent=4)




# this a function i made by using re to validate the date
def validate_date(date):
    # Regex pattern for YYYY-MM-DD
    pattern = r"^(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    
    if re.fullmatch(pattern, date):
        return True
    return False



def create_project(user_email):
    data = load_projects()  

    title  = input("Enter the title of the project here ")
    details = input("Enter the project details here ")
    target = input("Enter the total target Amount here ")
    try:
        target = float(target)
        if target <= 0:
            raise ValueError("Target amount must be greater than 0 ")
    except ValueError as e:
        print(f"Invalid target amount: {e} ")
        return
    
    start_date = input("Enter the start data yyyy-mm-dd ")
    end_date = input("Enter the end data dd- yyyy-mm-dd ") 


    if not validate_date(start_date) or not validate_date(end_date):
        print("please enter a valid date ")
        return

    project = {
        "owner": user_email,
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date
    }

    data.append(project)
    save_data(data)
    print("Project created successfully!")



def view_projects():
    projects = load_projects()
    if not projects:  
        print("No projects founded ")
        return
    for project in projects:
        print("*" * 40)
        print("-" * 40)
        print(f"title: {project.get('title', 'null')}")
        print(f"details: {project.get('details', 'null')}")
        print(f"target: {project.get('target', 'null')}")
        print(f"start Date: {project.get('start_date', 'null')}")
        print(f"end Date: {project.get('end_date', 'null')}")
        print(f"owner: {project.get('owner', 'null')}")




def find_project_by_title(projects, title, owner):
    for project in projects:
        if project["title"] == title and project["owner"] == owner:
            return project
    return None



def edit_project(user_email):
    projects = load_projects()
    edit_title = input("Enter the title of the project you want to edit: ")

    project = find_project_by_title(projects, edit_title, user_email)
    if project:
        print("Editing project...")
        project["title"] = input("Enter new title: ")
        project["details"] = input("Enter new details: ")
        try:
            project["target"] = float(input("Enter new target amount: "))
        except ValueError:
            print("Invalid target amount.")
            return
        project["start_date"] = input("Enter new start date (YYYY-MM-DD): ")
        project["end_date"] = input("Enter new end date (YYYY-MM-DD): ")

        if not validate_date(project["start_date"]) or not validate_date(project["end_date"]):
            print("Invalid date format. Changes were not saved.")
            return

        save_data(projects)
        print("Project updated successfully!")
    else:
        print("Project not found or you are not the owner.")



def delete_project(user_email):
    projects = load_projects()
    delete_title = input("Enter the title of the project you want to delete: ")

    project = find_project_by_title(projects, delete_title, user_email)
    if project:
        projects.remove(project)
        save_data(projects)
        print("Project deleted successfully.")
    else:
        print("Project not found or you are not the owner.")



