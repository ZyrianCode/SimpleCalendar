from DateFiller import DateFiller;
date_filler = DateFiller();
date_filler.input_date();
date_filler.set_date();
date = date_filler.get_date();
from Calendar import Calendar;

from DateValidator import DateValidator;



date_validator = DateValidator(date);
date_validator.check_date();

calendar = Calendar();
calendar.set_date(date);
calendar.day_of_week();