from datetime import datetime


class Vector:

    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date
        self.data_list = []

    def conver_date_object(self):
        return datetime(self.year, self.month, self.date)
