#!/usr/bin/python

from data_info import DataInfo
from wifi_info import WiFiInfo



class TestInfo(DataInfo):
    elems_len = 7
    include_wifi = True

    def __init__(self):
        super(TestInfo, self).__init__()
        self.row_id = None
        self.user_id = None
        self.mall_id = None
        self.time_stamp = None
        self.longitude = None
        self.latitude = None
        self.wifi_infos = None

    def set_value(self, parts):
        self.row_id, self.user_id, self.mall_id, self.time_stamp, self.longitude, self.latitude, last_part = parts
        # self.row_id = int(self.row_id)
        # assert self.is_valid_coordinate(self.longitude)
        # assert self.is_valid_coordinate(self.latitude)
        # self.longitude = float(self.longitude)
        # self.latitude = float(self.latitude)
        wifi_info_dict = WiFiInfo.load_wifi_infos(last_part)
        self.wifi_infos = wifi_info_dict
    
    def get_key_value(self):
        return self.row_id

    def validate(self):
        assert self.is_valid_number(self.row_id)
        assert self.is_positive_number_with_prefix(self.user_id, 'u_')
        assert self.is_positive_number_with_prefix(self.mall_id, 'm_')
        assert self.is_valid_date(self.time_stamp)
        assert self.is_valid_coordinate(self.longitude)
        assert self.is_valid_coordinate(self.latitude)

        for wifi_id, wifi_info_list in self.wifi_infos.items():
            for wifi_info in wifi_info_list:
                wifi_info.validate()

    def serialize(self):
        return '%s\t%s\t%s\t%s\t%s\t%s' % (self.row_id, self.user_id[2:], 
            self.mall_id[2:], self.format_date_str(self.time_stamp), self.longitude, self.latitude)