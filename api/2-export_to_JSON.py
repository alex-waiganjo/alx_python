"""This program fetches employee data and exports it to both CSV and JSON format

"""
import csv, json, requests, sys

def get_employee_data(employee_id):
    # URL to fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # URL to fetch employee TO DO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        # Fetch employee data
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()
        
        # Fetch employee TO DO list
        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()
        
        return employee_data,todos_data
    
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_csv(employee_id, employee_name, todos_data):
    csv_filename = f"{employee_id}.csv"
    
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write the tasks data
        for todo in todos_data:
            csv_writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

def export_to_json(employee_id, employee_name, todos_data):
    json_filename = f"{employee_id}.json"
    json_data = {
        "USER_ID": [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": employee_name
            }
            for todo in todos_data
        ]
    }
    with open(json_filename, "w") as json_file:
        json.dump(json_data, json_file)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    employee_data, todos_data = get_employee_data(employee_id)
    
    # Extract employee information
    employee_name = employee_data.get("name")
    
    # Export data to csv
    export_to_csv(employee_id, employee_name, todos_data)
    print(f"Data exported to {employee_id}.csv")
    
    # Export data to JSON
    export_to_json(employee_id, employee_name, todos_data)
    print(f"Data exported to {employee_id}.json")

if __name__ == "__main__":
    main()