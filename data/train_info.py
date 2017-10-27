#!/usr/bin/python

from data_info import DataInfo
from wifi_info import WiFiInfo


class TrainInfo(DataInfo):
    elems_len = 6
    include_key = False
    include_wifi = True
        
    def __init__(self):
        super(TrainInfo, self).__init__()
        self.user_id = None
        self.shop_id = None
        self.time_stamp = None
        self.longitude = None
        self.latitude = None
        self.wifi_infos = None

    def set_value(self, parts):
        self.user_id, self.shop_id, self.time_stamp, self.longitude, self.latitude, last_part = parts
        # assert self.is_valid_coordinate(self.longitude)
        # assert self.is_valid_coordinate(self.latitude)
        # self.longitude = float(self.longitude)
        # self.latitude = float(self.latitude)
        wifi_info_dict = WiFiInfo.load_wifi_infos(last_part)
        self.wifi_infos = wifi_info_dict

    def validate(self):
        assert self.is_positive_number_with_prefix(self.user_id, 'u_')
        assert self.is_positive_number_with_prefix(self.shop_id, 's_')
        assert self.is_valid_date(self.time_stamp)
        assert self.is_valid_coordinate(self.longitude)
        assert self.is_valid_coordinate(self.latitude)

        for wifi_id, wifi_info_list in self.wifi_infos.items():
            for wifi_info in wifi_info_list:
                wifi_info.validate()

    def serialize(self):
        return '%s\t%s\t%s\t%s\t%s' % (self.user_id[2:], 
            self.shop_id[2:], self.format_date_str(self.time_stamp), self.longitude, self.latitude)