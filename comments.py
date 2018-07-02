from datetime import datetime

class Comment:

    comments = []
    def __init__(self, comment, author):

        self.comment = comment
        self.author = author


    def create_comment(self):

        if self.comment.strip() == '' or self.author.strip()=='':
            return 'comment or author cannot be empty'

        self.id =1 

        if len(self.comments)>0:
            self.id = len(self.comments) +1




        self.date_created = datetime.now()


        comment_dict = {

            'comment':self.comment,
            'author' : self.author,
            'comment_id': self.id,
            'date_created': self.date_created
        }
        
        self.comments.append(comment_dict)

        return  "comment succesfully created"






        
