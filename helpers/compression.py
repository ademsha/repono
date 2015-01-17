# -*- coding: utf-8 -*-
import os
import zipfile
from os.path import basename
from helpers.files import FilesHelper


class CompressionHelper:

    def __init__(self):
        pass

    @staticmethod
    def compress_all_contents_in_dir(target_dir_path, compressed_file_name):
        FilesHelper.create_dirs_if_not_present(target_dir_path)
        FilesHelper.create_dirs_if_not_present(compressed_file_name)
        compressed_file = zipfile.ZipFile(compressed_file_name + ".zip", 'w')
        for target_file in os.listdir(target_dir_path):
            file_path = os.path.join(target_dir_path, target_file)
            compressed_file.write(file_path, arcname=target_file)
        compressed_file.close()

    @staticmethod
    def compress_single_file(target_file_path, compressed_file_name):
        FilesHelper.create_dirs_if_not_present(target_file_path)
        FilesHelper.create_dirs_if_not_present(compressed_file_name)
        compressed_file = zipfile.ZipFile(compressed_file_name + ".zip", 'w')
        compressed_file.write(target_file_path, arcname=basename(target_file_path))
        compressed_file.close()