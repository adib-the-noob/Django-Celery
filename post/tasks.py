from time import sleep
from celery import shared_task

@shared_task
def notify_cutomers(message):
    print("Sending message to all customers")
    print(message)
    sleep(5)
    print("Message sent")