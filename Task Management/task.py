from task_state import TaskState
from user import User

class Task:
    def __init__(self, id, title, description, due_date, priority, assigned_user:User):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = TaskState.PENDING
        self.assigned_user = assigned_user
        
    def getId(self):
        return self.id
    def getTitle(self):
        return self.title
    def getDescription(self):
        return self.description
    def getDueDate(self):
        return self.due_date
    def getPriority(self):
        return self.priority
    def getStatus(self):
        return self.status
    def getAssignedUser(self):
        return self.assigned_user
    
    def setTitle(self, title):
        self.title = title
    
    def setDescription(self, description):
        self.description = description
        
    def setDueDate(self, dua_date):
        self.due_date = dua_date
    def setPriority(self, priority):
        self.priority = priority
    def setStatus(self, status):
        self.status = status
        
        
        