from todoist_api_python.api import TodoistAPI
api_token = 'ac6ec72a38a0590df35f986f6147d6f9b3e92622'
api = TodoistAPI(api_token)

for task in api.get_tasks():
    print(task)
     
