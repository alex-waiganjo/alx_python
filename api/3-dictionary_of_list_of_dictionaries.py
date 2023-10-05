import json, requests, sys

def get_employee_data(employee_id):
    # URL to fetch employee details for all employees
    employee_url = f"https://jsonplaceholder.typicode.com/users"
    
    try:
        # Fetch data for all employees
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()
        
        all_data = {}
        
        # Iterate over all employees
        for employee in employee_data:
            employee_id = employee["id"]
            employee_name = employee["name"]
            
            # Fetch to do list
            _, todos_data = fetch_todos(employee_id)
            
            # Extract completed tasks for the employee
            completed_tasks = [{"username": employee_name, "task": todo["title"], "completed": todo["completed"]} for todo in todos_data if todo["completed"]]
            
            all_data[employee_id] = completed_tasks
            
        return all_data
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)
        
def fetch_todos(employee_id):
    # URL to fetch employee's to do list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()
        
        return todos_data
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)
        
def main():
    all_data = get_employee_data()
    
    # Export data to json
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)

if __name__ == "__main__":
    main()