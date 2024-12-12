# Define your task data
task_ids = [1, 2, 3]
task_names = ["Task A", "Task B", "Task C"]
task_urgencies = ["High", "Medium", "Low"]

# Define the function to format and print tasks
def create_formatted_records(fmt):
    for i in range(3):
        task_id = task_ids[i]
        name = task_names[i]
        urgency = task_urgencies[i]
        print(f'{task_id:{fmt}} {name:{fmt}} {urgency:{fmt}}')

# Call the function with a desired format, e.g. 10 characters width
create_formatted_records(10)