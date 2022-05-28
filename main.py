from todoist_api_python.api import TodoistAPI
from weather_api import WeatherAPI

CONFIGURATION = {

}

def main():

    forcast = weather_client.daily_forcast(45.523064, -122.676483)
    # Find the Camping Project
    projects = todoist_client.get_projects()
    camping_project = None
    for project in projects:
        if project.name.lower() == 'camping':
            camping_project = project

    # # Find the Camping Tasks
    # tasks = client.get_tasks()
    # camping_taskings = []
    # for task in tasks:
    #     if task.project_id == camping_project.id:
    #         print(task.content)

    # Create a test tasks
    todoist_client.add_task(content='Testing Task', project_id=camping_project.id)
    print('Hello Bob')


if __name__ == "__main__":
    main()