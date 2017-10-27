#!/usr/bin/python

import re
import timeit

from shop_info import ShopInfo
from train_info import TrainInfo
from test_info import TestInfo

SHOPS_INDEX = 0
TRAIN_INFOS_INDEX = 1
TEST_INFOS_INDEX = 2

SHOPS_PATH = '/home/epcc/proj/tianchi/data/input/train-ccf_first_round_shop_info.csv'
TRAIN_INFOS_PATH = '/home/epcc/proj/tianchi/data/input/train-ccf_first_round_user_shop_behavior.csv'
TEST_INFOS_PATH = '/home/epcc/proj/tianchi/data/input/test-evaluation_public.csv'

SHOP_INFO_OUTOUT_PATH = '/home/epcc/proj/tianchi/data/output/shops.csv'
TRAIN_INFOS_OUTOUT_PATH = '/home/epcc/proj/tianchi/data/output/train_infos.csv'
TEST_INFOS_OUTOUT_PATH = '/home/epcc/proj/tianchi/data/output/test_infos.csv'

TRAIN_INFOS_WIFI_OUTOUT_PATH = '/home/epcc/proj/tianchi/data/output/wifi_infos_train.csv'
TEST_INFOS_WIFI_OUTOUT_PATH = '/home/epcc/proj/tianchi/data/output/wifi_infos_test.csv'

TRAIN_AND_WIFI_OUTOUT_PATH = '/home/epcc/proj/tianchi/data/output/train_and_wifi.csv'
TEST_AND_WIFI_OUTOUT_PATH = '/home/epcc/proj/tianchi/data/output/test_and_wifi.csv'

info_dict = {
    SHOPS_INDEX : (SHOPS_PATH, ShopInfo, SHOP_INFO_OUTOUT_PATH),
    TRAIN_INFOS_INDEX: (TRAIN_INFOS_PATH, TrainInfo, TRAIN_INFOS_OUTOUT_PATH, 
        TRAIN_INFOS_WIFI_OUTOUT_PATH, TRAIN_AND_WIFI_OUTOUT_PATH),
    TEST_INFOS_INDEX : (TEST_INFOS_PATH, TestInfo, TEST_INFOS_OUTOUT_PATH, 
        TEST_INFOS_WIFI_OUTOUT_PATH, TEST_AND_WIFI_OUTOUT_PATH)
}


def load_shop_infos():
    start = timeit.default_timer()
    file_path, cls_name, output_path = info_dict[SHOPS_INDEX]
    with open(file_path, 'r') as file_content, \
        open(output_path, 'w') as output_file:
        first_line = True
        line_number = 0

        for line in file_content:
            line = re.sub('\s+','',line)
            if first_line:
                cls_name.head = line
                first_line = False
            else:
                # print ('Current line: %d' % line_number)
                line_number += 1
                parts = line.split(',')
                assert len(parts) == cls_name.elems_len
                obj = cls_name()
                obj.set_value(parts)
                # obj.validate()

                output_str = obj.serialize()
                if not cls_name.include_key:
                    output_str = '%d\t%s' % (line_number, output_str)
                output_str = '%s\n' % (output_str)
                output_file.write(output_str)
    
    stop = timeit.default_timer()
    print('Duration: %s minutes. Total lines: %d' % (int(stop - start) / 60, line_number))


def load_file(index):
    if index == SHOPS_INDEX:
        load_shop_infos()
        return

    start = timeit.default_timer()
    file_path, cls_name, output_path, wifi_output_path, wifi_ref_output_path = info_dict[index]
    with open(file_path, 'r') as file_content, \
        open(output_path, 'w') as output_file, \
        open(wifi_output_path, 'w') as wifi_output_file, \
        open(wifi_ref_output_path, 'w') as wifi_ref_output_file:
        first_line = True
        line_number = 0
        wifi_number = 0

        for line in file_content:
            line = re.sub('\s+','',line)
            if first_line:
                cls_name.head = line
                first_line = False
            else:
                # print ('Current line: %d' % line_number)
                # if line_number == 1000:
                #     break
                line_number += 1
                parts = line.split(',')
                assert len(parts) == cls_name.elems_len
                obj = cls_name()
                obj.set_value(parts)
                # obj.validate()

                output_str = obj.serialize()
                key = obj.get_key_value() if cls_name.include_key else str(line_number)
                if not cls_name.include_key:
                    output_str = '%d\t%s' % (line_number, output_str)

                output_str = '%s\n' % (output_str)
                output_file.write(output_str)

                for wifi_id, wifi_info_list in obj.wifi_infos.items():
                    for wifi_info in wifi_info_list:
                        wifi_number += 1
                        wifi_output_file.write('%d\t%s\n' % (wifi_number, wifi_info.serialize()))
                        wifi_ref_output_str = '%s\t%d' % (key, wifi_number)
                        wifi_ref_output_str = '%s\n' % (wifi_ref_output_str)
                        wifi_ref_output_file.write(wifi_ref_output_str)

    stop = timeit.default_timer()
    print('Duration: %s minutes. Total lines: %d' % (int(stop - start) / 60, line_number))

