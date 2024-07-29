import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        
        user_response.raise_for_status()
        todos_response.raise_for_status()
        
        user = user_response.json()
        todos = todos_response.json()
        
        employee_name = user.get('name')
        total_tasks = len(todos)
        completed_tasks = [todo for todo in todos if todo.get('completed')]
        number_of_done_tasks = len(completed_tasks)
        
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError:
        print("Error processing data. Please check the employee ID and try again.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID")
