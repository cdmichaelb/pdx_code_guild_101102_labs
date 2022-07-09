from getpass import getpass # For password field.

profiles = {
    1: {"username":"admin", "password":"admin"},
    2: {"username":"fred", "password":"alex"},
}

# profile = {"username":"admin", "password":"admin"}
auth_username_attemt,auth_password_attempt = ("","")
valid_yes = ["yes", "y", "sure", "ya"]
valid_no = ["no", "n", "nope", "nah", "quit", "q"]
valid_yes_no = valid_yes + valid_no
try_again_input = ""
unauthenticated = True
auth_attempts = 1
create_new_user = True
create_new_user_input = ""
new_user_success = False
new_user_name = ""

def login(username_attemt, password_attempt, profile): # Function to attempt to Login
    if username_attemt == profile["username"] and password_attempt == profile["password"]: # Check if user name exists in dict.
        return True # Return true if exists.
    else:
        return False # Return false if not exists.

def create_user(create_username_attemt, profile): # Function to create user.
    new_password = ""
    def user_exists(check_username_attempt, profile): # Functionto check if user exists.
        for ids in profile: # Check each id in profile to see if user name exists.
            if check_username_attempt in profile[ids]["username"]: # If exists return true.
                return True
            else: # If not exists return false.
                return False
    if user_exists(create_username_attemt,profile): # Call function to check if user exist and if exists do following:
        print("Sorry user exists already, please try again") # Tell user.
        return False # Return false.
    else: # Does not exist.
        while new_password == "": # Verify valid input.
            new_password = getpass("Please enter a new password: ") # Get new password from user. Using getpass to hide field.
        new_user_dict = {"username":create_username_attemt,"password":new_password} # Create dict entre for new user and pass.
        profiles[len(profiles)+1] = new_user_dict  # Add new user and pass dict to profiles dict.
        print("Creation Success") # Tell user success.
        return True # Return true.


print("Welcome to the authentication server.\n") # Just so output looks clean in terminal.
while create_new_user: # Run create new user loop until done.
    while create_new_user_input not in valid_yes_no: # Check for valid input.
        create_new_user_input = input("Would you like to create a new user? ").lower() # Ask user if they want to create a new user.
    if create_new_user_input in valid_yes: # User wants to create a new user:
        create_new_user = False # Set variable to false so this doesn't run again.
        while new_user_success == False: # User has not successfully created a new account:
            while new_user_name == "": # Check for valid input.
                new_user_name = input("Please enter a new user name: ") # Get a user name from user.
            new_user_success = create_user(new_user_name, profiles) # Check if user exists and change new_user_success based on the return.
            if new_user_success == False: # User exists
                new_user_name = "" # Reset username so user can try again.
    else: # User is done or does not want to create new account.
        create_new_user = False # Set bool to false so we don't run again after done.

while unauthenticated: # Authentication is not yet successful.
    while auth_username_attemt == "": # Check valid input.
        auth_username_attemt = input("Please enter your username: ") # Ask user for username.
    while auth_password_attempt == "": # Check valid input.
        auth_password_attempt = getpass("Please enter your password: ") # User getpass to ask user for password without displaying it.
    for ids in profiles: # Check each id in profiles.
        if login(auth_username_attemt, auth_password_attempt, profiles[ids]): # If Login attempt is successful:
            print("Login successful.\n") # Tell user.
            unauthenticated = False # Authentication is successful. This is unneeded unless there was more to the program.
            quit() # Quit

    if auth_attempts == 3: # User gets three tries.
        print("Sorry you have used up all your authentication attempts, please try again later.\n") # Tell user they have used all of their tries.
        quit() # Quit
    while try_again_input not in valid_yes_no: # Check for valid input.
        try_again_input = input(f'''Login failed {auth_attempts} times. You can try {3-auth_attempts} times more. Would you like to try again? (Y/N)
> ''').lower() # Ask if user wants to try again. Tell them how many attempts they have left.
    if try_again_input in valid_no: # User does not want to try again.
        print("Please try again later.\n") # Tell user.
        quit() # Quit
    elif try_again_input in valid_yes: # User wants to try again.
        # Reset all variables to try again.
        auth_username_attemt,auth_password_attempt = ("","")
        try_again_input = ""
        auth_attempts = auth_attempts + 1 # Increase attempt counter by 1.

