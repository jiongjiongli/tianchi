#!/usr/bin/python

from data_info import DataInfo


class ShopInfo(DataInfo):
    elems_len = 6
    
    def __init__(self):
        super(ShopInfo, self).__init__()
        self.shop_id = None
        self.category_id = None
        self.longitude = None
        self.latitude = None
        self.price = None
        self.mall_id = None

    def set_value(self, parts):
        self.shop_id, self.category_id, self.longitude, self.latitude, self.price, self.mall_id = parts
        # assert self.is_valid_coordinate(self.longitude)
        # assert self.is_valid_coordinate(self.latitude)
        # self.longitude = float(self.longitude)
        # self.latitude = float(self.latitude)
        # self.price = int(self.price)

    def get_key_value(self):
        return self.shop_id

    def validate(self):
        assert self.is_positive_number_with_prefix(self.shop_id, 's_')
        assert self.is_positive_number_with_prefix(self.category_id, 'c_')
        assert self.is_valid_coordinate(self.longitude)
        assert self.is_valid_coordinate(self.latitude)
        assert self.is_valid_number(self.price)
        assert self.is_positive_number_with_prefix(self.mall_id, 'm_')

    def serialize(self):
        return '%s\t%s\t%s\t%s\t%s\t%s' % (self.shop_id[2:], 
            self.category_id[2:], self.longitude, self.latitude, self.price, self.mall_id[2:])

