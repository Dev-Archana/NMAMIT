# CPU TASK MANAGEMENT USING QUEUE:
# dEFINE TASK CLASS
import time
class Task:
    def __init__(self,task_id,task_name,burst_time):
        self.task_id=task_id
        self.task_name=task_name 
        self.burst_time=burst_time 

    def __str__(self): # this method is used to print the string format of the given object
        # print(self.task_id)
        return f"TaskID:{self.task_id},Name:{self.task_name},Burst Time:{self.burst_time}"
# Create a task queue using list 
task_queue=[] 
# Add task method
def add_task(task_id,task_name,brust_time):
    task=Task(task_id,task_name,brust_time)
    task_queue.append(task)
    print(f"Task Added:{task}")
# Function to execute tasks (FCFS)
def execute_tasks():
    print("\n--- Starting Task Execution ---\n")
    while task_queue:
        task = task_queue[0]       # Get the first task
        task_queue.pop(0)          # Remove from front (O(n) operation)
        print(f"Executing {task}")
        time.sleep(task.burst_time)
        print(f"Completed: {task.task_name}\n")
    print("--- All Tasks Completed ---")


add_task(1,"compile code",2)
add_task(2,"Run tests",3)
add_task(3,"deploy application",2)

execute_tasks()