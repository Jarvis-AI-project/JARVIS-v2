from todoist_api_python.api import TodoistAPI
api_token = 'ac6ec72a38a0590df35f986f6147d6f9b3e92622'
api = TodoistAPI(api_token)

print(api.get_section(103223553))

# print('\n\n')
# for project in api.get_projects():
#     print(project)

# print(api.get_tasks('6162617675'))