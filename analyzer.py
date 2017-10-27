#!/usr/bin/python

from data.data_loader import load_file, SHOPS_INDEX, TRAIN_INFOS_INDEX, TEST_INFOS_INDEX

if __name__ == '__main__':
    load_file(SHOPS_INDEX)
    load_file(TRAIN_INFOS_INDEX)
    load_file(TEST_INFOS_INDEX)

