# pip install todoist-api-python
# https://developer.todoist.com/rest/v2/?python
# https://appdividend.com/2022/06/02/how-to-convert-python-list-to-json/


from todoist_api_python.api import TodoistAPI
import json
import datetime

api_token = 'ac6ec72a38a0590df35f986f6147d6f9b3e92622'
api = TodoistAPI(api_token)

def get_all_tasks_json():
    tasks_dict = {}
    task_values = {}
    tasks = api.get_tasks() # get all tasks
    for task in tasks:  # loop through tasks
        list_task = str(task)[5:].split(', ') # convert task to list with 
        for task_value in list_task:
            task_value_list = task_value.split('=')
            try:
                task_values[task_value_list[0]] = task_value_list[1]
            except Exception as e:
                print(e)
                print(task_value_list)
                break
        tasks_dict[task_values['id']] = task_values
    return tasks_dict
        

def get_all_tasks_txt():
    with open('tasks.txt', 'w') as f:
        f.write('')
        f.close()
    tasks = api.get_tasks() # get all tasks
    for task in tasks:  # loop through tasks
        with open('tasks.txt', 'a') as f:
            f.write(str(task))
            f.write('\n\n')
            f.close()

out = get_all_tasks_json()

json.dump(out, fp=open('tasks.json', 'w'), indent=4)

get_all_tasks_txt()