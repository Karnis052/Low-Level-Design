from task_manager import TaskManager
from user import User
from task import Task
from datetime import datetime

class TaskManagerDemo:
    @staticmethod
    def run():
        task_manager = TaskManager.getInstance()
        
        user1 = User("1", "Karnis", 'karnis@gmail.com')
        user2 = User('2', "Fatema", "fatema@gmail.com")
        
        #create tasks
        task1  = Task('1', 'Task 1', 'Description 1', datetime.now(), 1, user1)
        task2  = Task('2', 'Task 2', 'Description 2', datetime.now(), 1, user2)
        task3  = Task('3', 'Task 3', 'Description 3', datetime.now(), 2, user1)
        
        task_manager.createTask(task1)
        task_manager.createTask(task2)
        task_manager.createTask(task3)
        
        task3.setDescription("Updated Description")
        task_manager.updateTask(task3)
        
        #Search By keyword
        search_result = task_manager.searchTasks("Task")
        for task in search_result:
            print(task.getTitle())
        
        task_manager.markTaskAsCompleted('1')
        
        #Task History
        task_history = task_manager.getTaskHistory(user1)
        print("Task history for user")
        for task in task_history:
            print(task.getTitle())
            
            
        task_manager.deleteTask('3')
        
if __name__ == "__main__":
    TaskManagerDemo.run()
    
        