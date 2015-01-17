from tinydb import TinyDB, where
from config.app import AppConfig
from helpers.files import FilesHelper


class TinyDBApi:

    _databases = {}

    def __init__(self):
        data_file_locations = AppConfig.get_tinydb_files_paths()
        for data_file_location in data_file_locations.items():
            FilesHelper.create_dirs_if_not_present(data_file_location[1])
            self._databases[data_file_location[0]] = TinyDB(data_file_location[1])
        pass

    def get_db(self, name):
        return self._databases[name]

    @staticmethod
    def get_where():
        return where