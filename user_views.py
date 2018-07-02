from user_model import User

users = []


def signup(username, password, conf_password, user_category='normal'):
    if password.strip() == '' or username.strip() == '':
        return 'username or password cannot be empty'
    if not password == conf_password:
        return 'passwords provided do not match'
    # check whether user exists
    user_exists = [user for user in users if user['username'] == username]

    if len(user_exists) > 0:
        return 'user already exists'
    else:
        # create a user now and add him/her to the in-memory database
        user_object = User(username, password, user_category)
        users.append(user_object.__dict__)

        return 'Account created successfully'
