![Django](https://img.shields.io/badge/Django-3.x-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Postgres](https://img.shields.io/badge/Postgres-12.x-blue)
![Django Rest Framework](https://img.shields.io/badge/DRF-3.x-red)

# Github Manager in Django



## Features


## Requirements

- Python 3.12
- Django 5.1.4
- Django Rest Framework
- Postgresql

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/apfirebolt/django_movie_api.git
    cd django_movie_api
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Deployment

## Integration with Django with Celery for Cron jobs.

If you make any changes to the cron job, it is possible that some execution order of those functions might already have been pushed in the queue. You need to clear queues first and then stop both celery-beat and celery-worker.

In my case, I'm using Redis so I'd simply find all the keys which begin with Celery and would delete those keys kicking off a fresh re-start.

```
redis-cli KEYS "celery*" | xargs redis-cli DEL
```

```
# Stop Celery Beat
celery -A django_github beat --shutdown

# Stop Celery Workers
celery -A django_github worker --shutdown
```

Here, in this project a sample cron-job is spawned which prints all usernames in a text file every minute. The cron-job is inside tasks.py in github app. 

```Python
from celery import shared_task
from celery.utils.log import get_task_logger
from accounts.models import CustomUser

logger = get_task_logger(__name__)

@shared_task
def github_task():
    logger.info("Github Task")
    users = CustomUser.objects.all()
    usernames = [user.username for user in users]
    
    with open('usernames.txt', 'w') as file:
        for username in usernames:
            file.write(f"{username}\n")
            logger.info(f"User: {username}")
    
    return "Github Task Completed"
```

