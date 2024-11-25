import json 
import validation

def load_data(file_name = "data.json"):
    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []                       # lw el file msh mwgoud n return empty list
    except Exception as e:
        print(e)
        return []
    
def save_data(data,file_name="data.json"):
    with open(file_name,"w") as file:
        json.dump(data,file,indent=4)    # (dump >> we use it to convert the data to json from list or any type) ,, (ident >> to make the file json lines more readable)




def register_user():
    data = load_data()

    first_name = input("Enter the First name here ")
    last_name = input("Enter the Last name here ")
    email = input("Enter the email Here")
    password = input("Enter the password Here")
    confirm_password = input("Enter the password Again")
    phone = input("Enter the phone number Here")


    if not validation.validate_name(first_name) or not validation.validate_name(last_name):
        print("Please enter a valid name")
        return
    if not validation.validate_email(email):
        print("Please enter a valid email")
        return
    if not validation.validate_password(password, confirm_password):
        print("Please enter a valid password")
        return
    if not validation.validate_phone(phone):
        print("Please enter a valid phone number")
        return

    
    # any >> to look for all emails >> without using any we can make a for loop to loop in emails
    if any(user.get("email") == email for user in data):
        print("Email already exists.")
        return
    
    user = {
        "first_name":first_name,
        "last_name":last_name,
        "email":email,
        "password":password,
        "phone":phone
    }

    data.append(user)
    save_data(data) 
    print("User registered successfully")



def login_user():
    data = load_data()
    email = input("Enter the email Here: ")
    password = input("Enter the password Here: ")

    for user in data:
        if user["email"] == email and user["password"] == password:
            print("Login successful")
            return email 
    print("Login failed.")
    return None

