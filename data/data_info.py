#!/usr/bin/python

import re, datetime

pattern = re.compile(r"^-?\d{0,10}.\d{0,6}$")

class DataInfo(object):
    head = None
    elems_len = 0
    include_key = True
    include_wifi = False
    
    def __init__(self):
        super(DataInfo, self).__init__()

    def set_value(self, parts):
        pass

    def get_key_value(self):
        pass

    def is_valid_coordinate(self, coordinate_str):
        match_res = pattern.match(coordinate_str)
        if match_res is not None and float(coordinate_str) <= 0:
            print 'Wrong coordinate: %s' % (coordinate_str)
        return match_res is not None

    def serialize(self):
        pass

    def is_positive_number_with_prefix(self, number_str, prefix):
        res = (number_str[:2] == prefix) and self.is_positive_number(number_str[2:])
        if not res:
            print ('String: %s Prefix: %s %s %s' % (number_str, prefix, (number_str[:2] == prefix), is_valid_number(number_str[2:])))
        return res

    def is_positive_number(self, number_str):
        number = int(number_str)
        return number < 2147483647 and number > 0

    def is_valid_number(self, number_str):
        number = int(number_str)
        return number < 2147483647 and number > -2147483648

    def is_valid_date(self, date_str):
        try:
            date_value = datetime.datetime.strptime(date_str, '%Y-%m-%d%H:%M')
            return True
        except ValueError:
            return False

    def format_date_str(self, date_str):
        date_value = datetime.datetime.strptime(date_str, '%Y-%m-%d%H:%M')
        return date_value.strftime('%Y-%m-%d %H:%M')

    def validate(self):
        pass