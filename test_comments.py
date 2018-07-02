import unittest
from comments import Comment


class TestComments(unittest.TestCase):

    def setUp(self):
        self.comment = 'hey you'
        self.author = 'larry'

        self.wrong_coment = ''
        self.wrong_author = ''

    def test_create_comments_with_correct_details(self):
        results = Comment(self.comment, self.author).create_comment()

        self.assertEqual(results, "comment succesfully created")

    def test_create_comments_with_no_comment(self):
        results = Comment(self.wrong_coment, self.author).create_comment()
        self.assertEqual(results, "comment or author cannot be empty")

    def test_create_comment_with_no_author(self):
        results = Comment(self.comment, self.wrong_author).create_comment()
        self.assertEqual(results, "comment or author cannot be empty")
