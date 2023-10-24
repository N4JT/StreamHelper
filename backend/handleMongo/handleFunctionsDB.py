import eel
from mongodb import connect_to_mongodb  
from rememberLogin.generateKey import generateKey
from os_interaction.saveToAppdata import loadData,saveData,removeData
collection = connect_to_mongodb()

@eel.expose
def register_user(username, password,email):
    existing_email = user.find_one({"email":email})
    existing_username = users.find_one({"username": username})
    if existing_username:
        return False, "Username already exists"
    if existing_email:
        return False, "Email already registered"
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Insert the new user into the database
    users.insert_one({"username": username, "password": password,"email":email,"refreshKey":"","TwitchToken":"","YoutubeToken":""})
    return True, "Registration successful"
    
def update_user(username, parameter, new_value):
    user = collection.find_one({"username": username})
    if user:
        updated_data = {"$set": {parameter: new_value}}
        collection.update_one({"username": username}, updated_data)
        return True, "User information updated successfully"
    else:
        return False, "User not found"

@eel.expose  
def login(username, password,rememberedLogin):
    user = collection.find_one({"username": username})
    if user and password== user["password"]:
        if(rememberedLogin):
            refreshKey = generateKey()
            saveData(refreshKey)
            update_user(user["username"],"refreshKey",refreshKey)
        return "success"
    else:
        return False, "Login failed. Please check your credentials."
@eel.expose        
def javascriptPreLogin():
    if has_user_autologin():
        return "success"
    else:
        return "NotAutoLogin"

def has_user_autologin():
    data = loadData()
    if data:
        user = collection.find_one({"refreshKey":data})
        print(user["username"])
        if user:
            result = login(user["username"],user["password"],False)
            return result
    return False
@eel.expose 
def logout_user():
    removeData()
    return "success"

