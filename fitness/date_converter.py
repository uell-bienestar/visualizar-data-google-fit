"""
This class will convert dates to milliseconds and vice versa
https://stackoverflow.com/questions/9637838/convert-string-date-to-timestamp-in-python
https://www.programiz.com/python-programming/datetime/timestamp-datetime

"""

import time 
import datetime

class DateConverter():

    one_day = 86400000 # milliseconds in one day

    def convert_to_milliseconds(self, date):
        milliseconds = datetime.timestamp(date)
        return milliseconds

    def convert_to_date(self, milliseconds):
        dt_object - datetime.fromtimestamp(milliseconds)
        return dt_object