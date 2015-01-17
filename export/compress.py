# -*- coding: utf-8 -*-
import datetime

from config.app import AppConfig
from helpers.compression import CompressionHelper


class Compress:
    _config = None
    _dataApi = None
    _csv_dir_path = None
    _compressed_dir_path = None
    _db_file_locations = None
    _db_dir = None
    _compress_db_naming_prefix = None
    _compress_csv_naming_prefix = None

    def __init__(self):
        self._config = AppConfig.get_export_config()
        self._csv_dir_path = self._config["csv"]["export_dir"]
        self._compressed_dir_path = self._config["compression"]["export_dir"]
        self._compress_db_naming_prefix = self._config["compression"]["compress_db_naming_prefix"]
        self._compress_csv_naming_prefix = self._config["compression"]["compress_csv_naming_prefix"]
        self._db_file_locations = AppConfig.get_tinydb_files_paths()
        self._db_dir = AppConfig.get_tinydb_files()
        pass

    def compress_all_tinydb(self):
        compressed_file_path = self._compressed_dir_path + \
                               self._compress_db_naming_prefix \
                               + datetime.datetime.utcnow().strftime('%Y-%m-%d_%H-%M')
        CompressionHelper.compress_all_contents_in_dir(self._db_dir["database_dir"], compressed_file_path)

    def compress_tinydb(self, target):

        for data_file_location in self._db_file_locations.items():
            if data_file_location[0] == target:
                compressed_file_path = self._compressed_dir_path + self._compress_db_naming_prefix + target + "_" + datetime.datetime.utcnow().strftime(
                    '%Y-%m-%d_%H-%M')
                CompressionHelper.compress_single_file(data_file_location[1], compressed_file_path)

    def compress_all_csv(self):
        compressed_file_path = self._compressed_dir_path + self._compress_csv_naming_prefix + datetime.datetime.utcnow().strftime(
            '%Y-%m-%d_%H-%M')
        CompressionHelper.compress_all_contents_in_dir(self._csv_dir_path, compressed_file_path)