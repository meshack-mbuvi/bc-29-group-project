from datetime import datetime
from user_model import User


users = []
logged_in_users = []


def signup(username, password, conf_password, user_category='normal'):
    user_exists = [user for user in users if user['username'] == username]

    if len(user_exists) > 0:
        return 'user already exists'
    else:
        # create a user now and add him/her to the in-memory database
        user_object = User(username, password, user_category)
        users.append(user_object.__dict__)

        return 'Account created successfully'


def login(username, password):

    if password.strip() == '' or username.strip() == '':
        return 'username or password cannot be empty'
    print(users)
    user = [user for user in users if user['username']\
            == username and user['password'] == password]

    if user:
        current_user = user[0]['username']
        user[0]['last_login'] = datetime.now()
        # del users[0]
        users.append(user[0])
        logged_in_users.append(current_user)
        message = "succefully logged in as {}".format(current_user)

        return message
    return 'User does not exist'
