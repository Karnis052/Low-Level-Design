from datetime import datetime
from typing import List
from tag import Tag
from vote import Vote
from votable import Votable
from commentable import Commentable

class Question(Votable, Commentable):
    def __init__(self, author, title, content, tags_names):
        self.id = id(self)
        self.author = author
        self.title = title
        self.content = content
        self.creation_date = datetime.now()
        self.tags = [Tag(name) for name in tags_names]
        self.answers =[]
        self.comments = []
        self.votes = []
        
        
    def addAnswer(self, answer):
        if answer not in self.answers:
            self.answers.append(answer)
    
    def vote(self, user, value):
        if value not in [-1, 1]:
            raise ValueError("Value must be either 1 or -1")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        self.author.updateReputation(value*5)
    
    def getVoteCount(self):
        return sum(v.value for v in self.votes)
    
    def addComment(self, comment):
        self.comments.append(comment)
    
    def getComments(self):
        return self.comments.copy()
    