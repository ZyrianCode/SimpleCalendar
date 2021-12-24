from Date import Date;

class DateFiller(object):

    __day = 0;
    __month = 0;
    __year = 0;

    #__date = Date(__day, __month, __year);
    __date = Date();

    def input_date(self): 
        print("Введите день:");
        self.__day = input();
        print("Введите месяц:");
        self.__month = input();
        print("Введите год:");
        self.__year = input();

    

    def set_date(self): self.__date.set_date(self.__day, self.__month, self.__year);
    def get_date(self): return self.__date;



