import requests
from sys import argv


# def get_data(id):
#     user_data_url = f'https://jsonplaceholder.typicode.com/users/{id}'
#     user_todos_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
#     output = 0

#     # Fetch user data
#     user_data = requests.get(user_data_url)
#     user_todo = requests.get(user_todos_url)

#     # Parse user data
#     json_output = user_data.json()
#     emp_name = json_output["name"]
#     p = user_todo.json()
#     total = len(p)

#     # Display the titles of completed tasks
#     m = []
#     for task in user_todo.json():
#         if task["completed"]:
#             output += 1
#             m.append(task["title"])

#     # Display employee TODO list progress
#     print(f'Employee {emp_name} is done with tasks ({output}/{total}):')
#     for task_title in m:
#         print(f'\t{task_title}')


# if __name__ == '__main__':
#     if len(sys.argv) != 2:
#         print("Usage: python3 script_name.py employee_id")
#         sys.exit(1)

#     id = int(sys.argv[1])
#     get_data(id)


# def get_data(id):
#     user_data_url = f'https://jsonplaceholder.typicode.com/users/{id}'
#     user_todos_url= f'https://jsonplaceholder.typicode.com/users/{id}/todos'
#     output = 0
#     user_data = requests.get(user_data_url)
#     user_todo = requests.get(user_todos_url)
#     json_output= user_data.json()
#     emp_name = json_output["name"]


#     user_todo.json()
#     fr = user_todo.json()
#     total_no =  len(fr)

#     m = []


#     fr = user_todo.json()
#     for items in range(len(fr)):
#         nose= fr[items]["title"]
#         nos= fr[items]["completed"]
#         if nos:
#             output+=1
#             m.append(nose)
#             for v in m:
#                 print(v)
#     print(f'Employee {emp_name} is done with tasks ({output}/{total_no})')


import requests
# from sys import argv

# Get the user_id from the command line arguments
user_id = argv[1]

# Define the endpoint URL to access specific todo items for the user
url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

# Define the endpoint URL to get specific employee details
url_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

# Make an API request to retrieve user data
user_data = requests.get(url_user)
res = user_data.json()
employeeName = res['name']

# Make an API request to retrieve todo items for the user
todos_response = requests.get(url_todos)
todo_data = todos_response.json()

# Initialize lists and counters
titles = []
completed = 0
totalTasks = 0

# Iterate through the todo items and count completed and not completed tasks
for x in todo_data:
    if (x["completed"] == True):
        completed += 1
        titles.append(x['title'])
    if (x['completed'] == False or x['completed'] == True):
        totalTasks += 1

# Display the employee's task information
print('Employee {} is done with tasks({}/{}):'
      .format(employeeName, completed, totalTasks))

# Display the titles of completed tasks with indentation
for title in titles:
    print(f'\t {title}')
