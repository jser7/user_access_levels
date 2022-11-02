# User Access Levels
# Get data from JSON file for passwords
# Import libraries, set a fernet key.
import cryptography
from cryptography.fernet import Fernet
import json
k = Fernet.generate_key()
fernet = Fernet(k)


# Open JSON file, and encrypt the json dictionary.
with open("json_dict.json", "r") as f:
    data = json.load(f)
encrypt_data = fernet.encrypt(str(data).encode())


print("Welcome to the system. Please input your name.")
name = input()
# User inputs their name, if their name is recognised in the dictionary then they have to
# Enter a password and they will get superior access
name_level_dict = {"Jaden": 3, "Leah": 2, "Guest": 1}


def password(level):
    # User enters their password
    print("Password required. Please input the  password.")
    passAttempt = input()
    decrypted = fernet.decrypt(encrypt_data).decode()
    # Decrypt the previously encrypted JSON dictionary, and turn it back into a dictionary
    json_acceptable_string = decrypted.replace("'", '"')
    d = json.loads(json_acceptable_string)

    # If the user's password attempt is equal to the password found in the json file, then give access
    if passAttempt == d["passwords"][str(level)]:
        print("valid access")
    else:
        print("invalid access")


def checkLevel(dict_name):
    # dictName is the name the user inputted at the start.
    # If dictName is found in the list of users in the system, then check their access level.
    if dict_name in name_level_dict:
        if name_level_dict[dict_name] > 1:
            password(name_level_dict[dict_name])
    else:
        print("Not recognised. Level 1 access granted.")


checkLevel(name)
