#!/usr/bin/python

from data_info import DataInfo

class ResultInfo(DataInfo):
    elems_len = 2
    
    def __init__(self):
        super(ResultInfo, self).__init__()
        self.row_id = None
        self.shop_id = None

        def set_value(parts):
        pass