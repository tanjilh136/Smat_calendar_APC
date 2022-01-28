import time

from plyer import notification

def notify(title, message):
    """
    Notification Reminder
    :param title:
    :param message:
    :return:
    """
    notification.notify(
        title=title,
        message=message,
        timeout=20
    )