class TaskNode:
    def __init__(self, title, priority=1, deadline=None):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.prev = None
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, title, priority=1, deadline=None):
        new_task = TaskNode(title, priority, deadline) 
        if not self.head:
            self.head = new_task
            self.tail = new_task
        else:
            self.tail.next = new_task
            new_task.prev = self.tail
            self.tail = new_task

    # Method to delete a task by title
    def delete_task(self, title):
        current = self.head
        while current:
            print(f"Checking: {current.title}")  
            if current.title == title:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return f"Task '{title}' deleted."    
            current = current.next
        return f"Task '{title}' not found."

    # Method to display all tasks in the list
    def display_tasks(self):
        # Start from the head of the list
        current = self.head
        while current:
            # Print the task details (priority, title, deadline)
            print(f"[{current.priority}] {current.title} - Deadline: {current.deadline}")
            # Move to the next task in the list
            current = current.next
            