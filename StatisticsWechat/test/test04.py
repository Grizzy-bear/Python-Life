class Date(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, data_string):
        year, month, day = map(int, data_string.split('-'))
        date1 = cls(year, month, day)
        return date1    

    def out_date(self):
        print(self.year)

r = Date.get_date("2016-8-6")
r.out_date()