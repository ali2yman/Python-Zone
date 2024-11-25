import re

def validate_email(email):
    '''
        ^ and $ >> match the start and the end of this string 
        [a-zA-Z0-9._%+-]+ >> valid in the first part on username
        @ >> required symbol 
        the last part matches the domain

    '''
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_password(password,confirm_password):
    if len(password) < 6:
        print("password must be 6 char at least")
        return False
    if password != confirm_password:
        print("password must be identical")
        return False
    return True


def validate_phone(phone):
    if len(phone) == 11 and phone.startswith(("010","011","012","015")) and phone.isdigit():
        return True
    return False


def validate_name(name):
    if not(name.isalpha()) and len(name) < 2: 
        return False
    return True







    
