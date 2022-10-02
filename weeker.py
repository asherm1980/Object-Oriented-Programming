class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    # Write code here.
    #

    def __init__(self, day):
        #
        # Write code here.
        #
        self.day=day
        self.weekdays=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        if self.day not in self.weekdays:
            raise WeekDayError
        self.__str__()
        


    def __str__(self):
        #
        # Write code here.
        #
        return self.day
        

    def add_days(self, n):
        #
        # Write code here.
        #
        self.dayindex=self.weekdays.index(self.day)
        self.day=self.weekdays[self.dayindex+(n%7)]
        self.__str__()
    def subtract_days(self, n):
        #
        # Write code here.
        #
        self.dayindex=self.weekdays.index(self.day)
        self.day=self.weekdays[self.dayindex-(n%7)]
        self.__str__()

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(2)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
