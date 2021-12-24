from Date import Date

class DateValidator(object):
    """description of class"""

    #__date = Date();

    def __init__(self, date): 
        #self.__date = date;
        self.__day = date.get_day();
        self.__month = date.get_month();
        self.__year = date.get_year();

        self.__is_31_day_valid = self.__day <= 31 and self.__day >= 1;
        self.__is_30_day_valid = self.__day <= 31 and self.__day >= 1;
        self.__is_february_day_valid = self.__day <= 28 and self.__day >= 1;
        self.__is_leap_year_february_day_valid = self.__day <= 29 and self.__day >= 1;

        self.__is_month_february = self.__month == 2;

        self.__is_month_contains_31_day = (self.__month == 1 or
        self.__month == 3 or self.__month == 5 or self.__month == 7 or self.__month == 8 or
        self.__month == 10 or self.__month == 12);
        self.__is_month_valid = self.__month >= 1 and self.__month <= 12;

        self.__is_leap_year = (self.__year % 4 == 0 and self.__year % 100 != 0) or (self.__year % 400 == 0);


    __day = 0;
    __month = 0;
    __year = 0;
    
    __is_31_day_valid = 0;
    __is_30_day_valid = 0;
    __is_february_day_valid = 0;
    __is_leap_year_february_day_valid = 0;

    __is_month_february = 0;

    __is_month_contains_31_day = 0;

    __is_leap_year = 0;

    def check_day(self):     

        if(self.__is_month_contains_31_day):
            if(not self.__is_31_day_valid): print("День должен входить в диапазон от 1 до 31 включительно!");

        elif(self.__is_month_february and self.__is_leap_year):
           if(not self.__is_leap_year_february_day_valid): print("День должен входить в диапазон от 1 до 29 включительно!");

        elif(self.__is_month_february and not __is_leap_year):
            if(not self.__is_february_day_valid): print("День должен входить в диапазон от 1 до 28 включительно!");

        elif(not self.__is_month_contains_31_day and not self.__is_month_february):
            if(not self.__is_30_day_valid): print("День должен входить в диапазон от 1 до 30 включительно!");
        else: print("Unknown error!");

    def check_month(self):    
        if(not self.__is_month_valid): print("Месяц должен входить в диапазон от 1 до 12 включительно!");

    def check_date(self):
        self.check_day();
        self.check_month();

