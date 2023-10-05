
import requests
import sys

def get_data(id):
    user_data_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    user_todos_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    output = 0
    
    # Fetch user data
    user_data = requests.get(user_data_url)
    user_todo = requests.get(user_todos_url)
    
    # Parse user data
    json_output = user_data.json()
    emp_name = json_output["name"]
    p = user_todo.json()
    total = len(p)

    # Display the titles of completed tasks
    m = []
    for task in user_todo.json():
        if task["completed"]:
            output += 1
            m.append(task["title"])
    
    # Display employee TODO list progress
    print(f'Employee {emp_name} is done with tasks ({output}/{total}):')
    for task_title in m:
        print(f'\t{task_title}')

if __name__ == '__main__':
     id = sys.argv[1]
     get_data(id)    





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
   
    
           
