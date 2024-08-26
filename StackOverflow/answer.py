from commentable import Commentable
from votable import Votable
from typing import List
from datetime import datetime
from vote import Vote

class Answer(Commentable, Votable):
    def __init__(self, author, question, content):
        self.id = id(self)
        self.author = author
        self.question = question
        self.content = content
        self.creation_date = datetime.now()
        self.votes = []
        self.comments = []
        self.is_accepted = False
        
    def vote(self, user, value):
        if value not in [-1, 1]:
            raise ValueError("Value must be either 1 or -1")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        self.author.updateReputation(value*10)
    def getVoteCount(self):
        return sum(v.value for v in self.votes)
    def addComment(self, comment):
        self.comments.append(comment)
    
    def getComments(self):
        return self.comments.copy()
    
    def accept(self):
        if self.is_accepted:
            raise ValueError("Already accepted")
        self.is_accepted = True
        self.author.updateReputation(15)