from user_views import *
from comments import Comment


def manage():
    while True:
        var = input("choose add or edit comment ...\n").lower()
        if var == "add":
            comment = input("Enter your comment ...\n")
            author = users[0]['username']
            comment_obj = Comment(comment, author)
            result = comment_obj.create_comment()
            print(result)
            comment_obj.show()
        if var == 'edit':
            comment_id = input('Enter comment id: ..')
            message = input("Enter comment message")
            com_object = [comment for comment in Comment.comments if comment[
                'comment_id'] == int(comment_id)]


while(True):
    var = input("Please login or signup ...\n").lower()
    if var == 'signup':
        username = input("Your username:...\n")
        password = input("your password:...\n")
        conf_password = input("confirmation password:...\n")
        user_cat = input("category:...\n")
        result = signup(username, password, conf_password, user_cat)
        print(result)

    if var == 'login':
        username = input("Your username:...")
        password = input("your password:...")
        result = login(username, password)
        if result == 'User does not exist':
            print("Account does not exist")
            continue
        else:
            manage()
