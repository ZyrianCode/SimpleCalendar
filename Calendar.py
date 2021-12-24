from Date import Date

class Calendar(object):

    __date = Date();

    def set_date(self, date): 
        self.__date = date;
        self.__day = date.get_day();
        self.__month = date.get_month();
        self.__year = date.get_year();

    __day = 0;
    __month = 0;
    __year = 0;

    __names = {0:"Воскресенье", 1:"Понедельник", 2:"Вторник", 3:"Среда", 4:"Четверг", 5:"Пятница", 6:"Суббота"};

    def convert_to_names(self, iso):
        print(self.__names.get(iso));

    def day_of_week(self):
        countOfMonthsInYear = 12;
        a = int((14 - self.__month) / countOfMonthsInYear);
        y = int(self.__year - a);
        m = int(self.__month + 12 * a - 2);
        iso = int((7000 + (self.__day + y + y / 4 
                          - y / 100 + y / 400 + (31 * m) / 12)) % 7);
        self.convert_to_names(iso);


