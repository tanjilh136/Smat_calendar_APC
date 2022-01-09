from datetime import datetime
from playsound import playsound

import Event
from Event import *


class Alarm:
    def __init__(self, date):
        self.date = date

    def alarm_rang(self):
        if datetime.now() == Event.Event.get_reminder_time():
            playsound("C:/Users/tanjil/PycharmProjects/pythonProject3/media/sound.mp3")



