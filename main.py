class Task:
    def __init__(self):
        self.task_list = {}

    def add_task(self, status="Not Completed"):
        task_name = input("Enter Task Name: ")
        task_discription = input("Enter Task Discription: ")
        due_date = input("Enter Due Date: ")
        self.task_list[task_name] = [task_discription, due_date, status]
        print(f"{task_name} - Task added successfully.")

    def change_status_task(self):
        task_name = input("Enter Task Name: ")
        if task_name in self.task_list.keys():
            self.task_list[task_name][2] = "Completed"
            print(f"{task_name} - Task status changed to completed.")
        else:
            print(f"{task_name} - Task not found.")

    def view_task_list(self):
        list_type = input("Enter list type (1. Full List, 2. Not Completed): ")
        if list_type == "1":
            for key, value in self.task_list.items():
                print(key, value)
        else:
            for key, value in self.task_list.items():
                if value[2] == "Not Completed":
                    print(key, value)

def manage_task():
    task_manager = Task()
    while True:
        your_choice = int(input("Enter your choice (1. Add_Task, 2.Change Task Status, 3. View Task List , 4. Exit): "))
        if your_choice == 1:
            task_manager.add_task()
        elif your_choice == 2:
            task_manager.change_status_task()
        elif your_choice == 3:
            task_manager.view_task_list()
        elif your_choice == 4:
            break

if __name__ == "__main__":
    manage_task()
