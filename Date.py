class Date(object):
    __day = 0; 
    __month = 0;
    __year = 0;
   
    def set_date(self, day, month, year): 
        self.__day = int(day);
        self.__month = int(month);
        self.__year = int(year);

    def get_day(self): return self.__day;
    def get_month(self): return self.__month;
    def get_year(self): return self.__year;
