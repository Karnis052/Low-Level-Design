from task import Task
from task_state import TaskState

class TaskManager:
    _instance = None
    
    def __init__(self):
        if TaskManager._instance is not None:
            raise Exception("This is a singleton")
        else:
            TaskManager._instance = self
            self.tasks = {}
            self.user_tasks = {}
    @staticmethod
    def getInstance():
        if TaskManager._instance is None:
            TaskManager()
        return TaskManager._instance
    
    def createTask(self, task):
        self.tasks[task.getId()] = task
        self.assignTaskToUser(task.getAssignedUser(), task)
    def updateTask(self, updated_task):
        existing_task = self.tasks.get(updated_task.getId())
        if existing_task:
            existing_task.setTitle(updated_task.getTitle())
            existing_task.setDescription(updated_task.getDescription())
            existing_task.setDueDate(updated_task.getDueDate())
            existing_task.setPriority(updated_task.getPriority())
            existing_task.setStatus(updated_task.getStatus())
            previous_user = existing_task.getAssignedUser()
            new_user = updated_task.getAssignedUser()
            if previous_user != new_user:
                self.unassignTaskFromUser(previous_user, existing_task)
                self.assignTaskToUser(new_user, updated_task)
                
    def deleteTask(self, task_id):
        task =self.tasks.pop(task_id, None)
        if task:
            self.unassignTaskFromUser(task.getAssignedUser(), task)
            
    def searchTasks(self, keyword):
        maching_task = []
        for task in self.tasks.values():
            if keyword in task.getTitle() or keyword in task.getDescription():
                maching_task.append(task)
        return maching_task

    def filterTasks(self, status, start_date, end_date, priority):
        filtered_tasks =[]
        for task in self.tasks.values():
            if(
                task.getStatus() == status
                and start_date <= task.getDueDate() <= end_date
                and task.getPriority() == priority
            ):
                filtered_tasks.append(task)
        return filtered_tasks
        
    def markTaskAsCompleted(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            task.setStatus(TaskState.COMPLETED)
        
    def getTaskHistory(self,user):
        return self.user_tasks.get(user.getId(), [])
    def assignTaskToUser(self, user, task):
        self.user_tasks.setdefault(user.getId(), []).append(task)
    
    def unassignTaskFromUser(self, user, task):
        tasks = self.user_tasks.get(user.getId())
        if tasks:
            tasks.remove(task)
        
        
            