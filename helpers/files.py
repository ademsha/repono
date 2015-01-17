# -*- coding: utf-8 -*-
import os


class FilesHelper:

    def __init__(self):
        pass

    @staticmethod
    def delete_all_contents_in_dir(target_dir_path):
        FilesHelper.create_dirs_if_not_present(target_dir_path)
        for target_file in os.listdir(target_dir_path):
            file_path = os.path.join(target_dir_path, target_file)
            FilesHelper.create_dirs_if_not_present(file_path)
            try:
                os.unlink(file_path)
            except Exception, e:
                print e

    @staticmethod
    def create_dirs_if_not_present(target_path):
        if not os.path.exists(os.path.dirname(target_path)):
            os.makedirs(os.path.dirname(target_path))