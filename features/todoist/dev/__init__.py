from todoist_api_python.api import TodoistAPI
import json

task_call = 'https://todoist.com/showTask?id='  # +id
api = TodoistAPI('ac6ec72a38a0590df35f986f6147d6f9b3e92622')


def get_project_name_by_id(project_id):
    try:
        project = api.get_project(project_id)
        print(project)
        return project['name']

    except Exception as e:
        print(e)
        return False

def convert_task_list_to_json(list_task):
    for task_value in list_task:

        try:
            # task-value list=['assignee_id', 'None']
            task_value_list = task_value.split('=')
            print(task_value_list)

        except Exception as e:
            print(e)
            return False

    return {0}


def get_overdue_tasks_dict():
    try:
        tasks = api.get_tasks()
        print('Total number of tasks : ', len(tasks))
        for task in tasks:
            # convert task to list with each object as a item
            list_task = str(task)[5:-1].split(', ')
            dict_task = convert_task_list_to_json(list_task)

            if dict_task == False:
                print('Error in convert_task_list_to_json')
                return False
            else:
                print(dict_task)

            break

        return {0}

    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    print(get_overdue_tasks_dict())


'''
task_list_sample = 
[
    'assignee_id=None', 
    'assigner_id=None', 
    'comment_count=1', 
    'is_completed=False', 
    "content='Maths practice page 1'", 
    "created_at='2022-09-11T06:19:24.623478Z'", 
    "creator_id='37026392'", 
    "description=''", 
    'due=None', 
    "id='6162617675'", 
    'labels=[]', 
    'order=0', 
    'parent_id=None', 
    'priority=1', 
    "project_id='2300111701'", 
    "section_id='103223553'", 
    "url='https://todoist.com/showTask?id=6162617675'", 
    'sync_id=None'
]
'''
