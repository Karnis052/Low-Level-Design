from question import Question
from answer import Answer
from comment import Comment

class User:
    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email
        self.reputation = 0
        self.questions = []
        self.answers = []
        self.comments = []
    
    def askQuestion(self, title, content, tags):
        question = Question(self, title, content, tags)
        self.questions.append(question)
        self.updateReputation(5)
        return question
    
    def answerQuestion(self, question, content):
        answer = Answer(self, question, content)
        self.answers.append(answer)
        self.updateReputation(10)
        return answer
    def commentOn(self, commentable, content):
        comment = Comment(self, content)
        self.comments.append(comment)
        commentable.addComment(comment)
        self.updateReputation(2)
        return comment
        
        
    def updateReputation(self, value):
        self.reputation += value
        self.reputation = max(0, self.reputation)