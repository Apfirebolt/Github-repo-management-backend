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
