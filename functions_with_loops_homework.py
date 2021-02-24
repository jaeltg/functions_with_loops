tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks(task_list):
    tasks_filtered = []
    for task in task_list:
        if task["completed"] == False:
            tasks_filtered.append(task)
    return tasks_filtered
tasks_uncompleted = uncompleted_tasks(tasks) 
# print(tasks_uncompleted)     

def completed_tasks(task_list):
    tasks_filtered = []
    for task in task_list:
        if task["completed"] == True:
            tasks_filtered.append(task)
    return tasks_filtered
tasks_completed = completed_tasks(tasks) 
# print(tasks_completed)  

def task_descriptions(task_list):
    tasks_filtered = []
    for task in task_list:
        tasks_filtered.append(task["description"])
    return tasks_filtered
description_of_tasks = task_descriptions(tasks)
# print(description_of_tasks)  

def certain_time(task_list, time):
    tasks_filtered = []
    for task in task_list:
        if task["time_taken"] >= time:
             tasks_filtered.append(task)
    return tasks_filtered   
task_time = certain_time(tasks, 50)
# print(task_time)

def given_description(task_list, description):
    for task in task_list:
        if task ["description"] == description:
            return task
task_specific = given_description(tasks, "Wash Dishes")
# print(task_specific)    

def given_description_mark_complete(task_list, description):
    for task in task_list:
        if task["description"] == description:
            task["completed"] = True
    return task
task_now_completed = given_description_mark_complete(tasks, "Wash Dishes")
# print(tasks) 

def add_task(task_list, description, completed, time):
    new_task = {"description": description, "completed": completed, "time_taken": time}
    task_list.append(new_task)
    return task_list
new_task_list = add_task(tasks, "Clean Room", True, 30)
# print(new_task_list)  

user_input = input("Select an option: ")
while user_input != None:
    if user_input == 1:
        print(tasks)
    elif user_input == 2:
        print(uncompleted_tasks)
    elif user_input == 3:
        print(completed_tasks)
    elif user_input == 4:
        print(given_description_mark_complete)
    elif user_input == 5:
        print(certain_time)
    elif user_input == 6:
        print(given_description)
    elif user_input == 7:
        print(add_task)
    elif user_input == "M" or "m":
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit") 
    elif user_input == "Q" or "q":
        break                            
    else:
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")    



