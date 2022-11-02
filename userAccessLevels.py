# User Access Levels
# Get data from JSON file for passwords
import json
import hashlib


# Open JSON file
with open("json_dict.json", "r") as f:
    data = json.load(f)


name = input()
# User inputs their name, if their name is recognised in the dictionary then they have to
# Enter a password and they will get superior access
name_level_dict = {"Jaden": 3, "Violet": 2, "Guest": 1}


def password(level):
    # User enters their password
    # Password is hashed, if it matches the hash found in the JSON file, the password is correct.
    print("Password required. Please input the  password.")
    pass_inp = input()
    hashed_pass = hashlib.sha512(pass_inp.encode())
    hash_pass_digest = hashed_pass.hexdigest()

    # Check password matches JSON file password
    if hash_pass_digest == data["passwords"][str(level)]:
        print("Access Granted")
    else:
        print("Access Denied")


def checkLevel(dict_name):
    # dict_name is the name the user inputted at the start.
    # If dict_name is found in the list of users in the system, then check their access level.
    if dict_name in name_level_dict:
        if name_level_dict[dict_name] > 1:
            password(name_level_dict[dict_name])
    else:
        print("Not recognised. Level 1 access granted.")


checkLevel(name)
