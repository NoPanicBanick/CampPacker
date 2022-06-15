from todoist_api_python.api import TodoistAPI
from weather_api import WeatherAPI
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

CONFIGURATION = {
    'kvurl': 'https://todocamp-kv.vault.azure.net/'
}

def start_up_app_config():
    # Startup Config
    creds = DefaultAzureCredential()
    secret_client = SecretClient(CONFIGURATION['kvurl'], creds)
    CONFIGURATION['weather_apikey'] = secret_client.get_secret('openweather-apikey').value
    CONFIGURATION['todoist_apikey'] = secret_client.get_secret('todoit-apikey').value
    return CONFIGURATION

def main():
    """Attempts to make a packing list off the weather"""
    CONFIG = start_up_app_config()
    weather_client = WeatherAPI(CONFIG['weather_apikey'])
    todoist_client = TodoistAPI(CONFIG['todoist_apikey'])
    
    # Main
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