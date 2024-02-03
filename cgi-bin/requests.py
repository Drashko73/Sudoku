import cgi                          # Support module for CGI (Common Gateway Interface) scripts
import json                         # JSON (JavaScript Object Notation) <https://json.org>
from pysqlite import Database       # Custom class for database comunication

database = Database()   # create database instance

get = cgi.FieldStorage()

# Listen for checking if any user is signed in
if 'check_login' in get:
    print("Content-type: application/json\n") 
    response = database.find_user_by_sessid(get["sessid"].value)
    print(json.dumps(response))

# Listen for register request
if "register_request" in get:
    print("Content-type: application/json\n") 
    response = database.register_user(get["info"].value)
    print(json.dumps(response))

# Listen for login request
if 'login_request' in get:
    print("Content-type: application/json\n") 
    response = database.login_user(get["email"].value, get["password"].value)
    print(json.dumps(response))

# Listen for logout request
if 'logout_request' in get:
    print("Content-type: application/json\n") 
    response = database.logout_user(get["sessid"].value)
    print(json.dumps(response))

# Listen for getting user information by email
if 'get_user_info' in get:
    print("Content-type: application/json\n")
    response = database.get_user_by_email(get["email"].value)
    print(json.dumps(response))

# Listen for updating player stats
if 'increase_total_completed' in get:
    print("Content-type: application/json\n") 
    response = database.increase_total_completed(get["email"].value, get["level"].value, get["time"].value)
    print(json.dumps(response))
    
# Listen for request for all users data
if 'get_all_users' in get:
    print("Content-type: application/json\n") 
    response = database.get_all_users()
    print(json.dumps(response))