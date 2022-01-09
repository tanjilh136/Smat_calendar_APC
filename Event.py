from Vector import *


class Event:
    def __init__(self):
        self.event_recorder = []

    def add_reminder(self, date):
        date_dic = {
            'time_of_reminder_set': (datetime.now().year, datetime.now().month, datetime.now().day()),
            'alarm_time': Vector.conver_date_object(date)
        }
        self.event_recorder.append(date_dic)

    def get_reminder_list(self):
        return self.event_recorder

    def get_reminder_time(self):
        time_of_reminder_set = (datetime.now().year, datetime.now().month, datetime.now().day())
        for i in self.event_recorder:
            if i['time_of_reminder_set'] == time_of_reminder_set:
                return i['alarm_time']

    def pop_reminder(self):
        time_of_reminder_set = (datetime.now().year, datetime.now().month, datetime.now().day())
        for i in self.event_recorder:
            if i['time_of_reminder_set'] == time_of_reminder_set:
                del i['time_of_reminder_set']

    def pop_reminder(self, date):
        time_of_reminder_set = Vector.conver_date_object(date)
        time_of_reminder_set = (time_of_reminder_set.year, time_of_reminder_set.month, time_of_reminder_set.day)
        for i in self.event_recorder:
            if i['time_of_reminder_set'] == time_of_reminder_set:
                del i['time_of_reminder_set']
