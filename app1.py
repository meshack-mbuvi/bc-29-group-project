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
        if var == 'edit':
            comment_id = input('Enter comment id: ..')
            message = input("Enter comment message")
            com_object = [comment for comment in Comment.comments if comment[
                'comment_id'] == int(id)]


while(True):
    var = input("Please login or signup ...\n").lower()
    if var == 'signup':
        username = input("Your username:...\n")
        password = input("your password:...\n")
        conf_password = input("confirmation password:...\n")
        conf_password = input("category:...\n")
        result = signup(username, password, conf_password)
        print(result)
    if var == 'login':
        username = input("Your username:...")
        password = input("your password:...")
        result = login(username, password)

        manage()
