import requests
import sys



def  get_data(id):
    user_data_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    user_todos_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    output = 0

    # Fetch  data
    user_data = requests.get(user_data_url)
    user_todo = requests.get(user_todos_url)

    # Parse data
    json_output = user_data.json()
    emp_name = json_output["name"]
    json_user_todo = user_todo.json()
    total_tasks = len(json_user_todo)

    # Display the titles of completed tasks
    m = []
    for task in user_todo.json():
        if task["completed"]:
            output += 1
            m.append(task["title"])


    print(f'Employee {emp_name} is done with tasks ({output}/{total_tasks}):')
    for task_title in m:
        print(f'\t{task_title}')


if __name__ =='__main__':
    id = sys.argv[1]
    get_data(id)