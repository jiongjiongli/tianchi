#!/usr/bin/python

from data_info import DataInfo

class WiFiInfo(DataInfo):
    elems_len = 3

    def __init__(self):
        super(WiFiInfo, self).__init__()
        self.wifi_id = None
        self.signal = None
        self.connected = None

    def set_value(self, parts):
        self.wifi_id, self.signal, self.connected = parts
        # self.signal = int(self.signal)
        # assert self.connected.lower() in ('True'.lower(), 'False'.lower())
        # self.connected = (self.connected.lower() == 'True'.lower())

    def get_key_value(self):
        return self.wifi_id

    def validate(self):
        assert self.is_positive_number_with_prefix(self.wifi_id, 'b_')
        assert self.is_valid_number(self.signal)
        assert self.connected.lower() in ('True'.lower(), 'False'.lower())


    @staticmethod
    def load_wifi_infos(infos_str):
        cls_name = WiFiInfo
        wifi_info_dict = {}
        parts = infos_str.split(';')

        for part in parts:
            wifi_info_parts = part.split('|')
            assert len(wifi_info_parts) == cls_name.elems_len
            wifi_info = cls_name()
            wifi_info.set_value(wifi_info_parts)
            key = wifi_info.get_key_value()
            wifi_info_dict.setdefault(key, [])
            wifi_info_dict[key].append(wifi_info)

        return wifi_info_dict

    def serialize(self):
        wifi_connected = '1' if (self.connected.lower() == 'True'.lower()) else '0'
        return '%s\t%s\t%s' % (self.wifi_id[2:], self.signal, wifi_connected)