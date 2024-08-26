from user import User
from typing import Dict
from question import Question
from answer import Answer
from comment import Comment
from tag import Tag

class StackOverflow:
    def __init__(self):
        self.users : Dict[int, User] = {}
        self.questions : Dict[int, Question] = {}
        self.answers: Dict[int, Answer] = {}
        self.tags : Dict[str, Tag] = {}

    def createUser(self, username, email):
        user_id = len(self.users)+1
        user = User(user_id, username, email)
        self.users[user_id] = user
        return user
    def askQuestion(self, user, title, content, tags):
        question = user.askQuestion(title, content, tags)
        self.questions[question.id] = question
        for tag in question.tags:
            self.tags.setdefault(tag.name, tag)   
        return question
    
    def answerQuestion(self, user, question, content):
        answer = user.answerQuestion(question, content)
        self.answers[user.id] = answer
        return answer
    def addComment(self, user,commentable, content):
        return user.commentOn(commentable, content)
    def voteQuestion(self, user, question, value):
        question.vote(user, value)
    def voteAnswer(self, user, answer, value):
        answer.vote(user, value)
    def acceptAnswer(self, answer):
        answer.accept()
        
    def searchQuestions(self, query):
        question = []
        for q in self.questions.values():
            if (query.lower() in q.title.lower() or   
                query.lower() in q.content.lower() or 
                any(query.lower() == tag.name.lower() for tag in q.tags)):
                question.append(q)
                
        return question
    def getQuestionsByUser(self, user):
        return user.questions
    
    def getUser(self, user_id):
        return self.users.get(user_id)
    
    def getQuestion(self, ques_id):
        return self.questions.get(ques_id)
    
    def getAnswer(self, answer_id):
        return self.answers.get(answer_id)
    
    def getTag(self, name):
        return self.tags.get(name)
            
            
        