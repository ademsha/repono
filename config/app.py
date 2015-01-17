import json
from tweepy import TweepError


class AppConfig:
    def __init__(self):
        pass

    @staticmethod
    def get_twitter_auth():
        with open('config/auth.json') as target_file:
            data = json.load(target_file)
            consumer_key = data["twitter"]["consumer_key"]
            consumer_secret = data["twitter"]["consumer_secret"]
            if consumer_key == "" or consumer_secret == "":
                raise TweepError('Expected consumer_key and consumer_secret'
                                 ' from auth.js but found empty values')
            else:
                return consumer_key, consumer_secret

    @staticmethod
    def get_tinydb_files():
        with open('config/config.json') as target_file:
            data = json.load(target_file)
            locations = {}
            for data_location in data["data_storage"]["tinydb"].items():
                locations[data_location[0]] = data_location[1]
            return locations

    @staticmethod
    def get_tinydb_files_paths():
        with open('config/config.json') as target_file:
            data = json.load(target_file)
            config, locations = {}, {}
            for value in data["data_storage"]["tinydb"].items():
                config[value[0]] = value[1]
            database_dir = config["database_dir"]
            for data_file_location in config["databases"].items():
                locations[data_file_location[0]] = database_dir + data_file_location[1]
            return locations

    @staticmethod
    def get_queries_config(provider):
        with open('config/config.json') as target_file:
            data = json.load(target_file)
            config = {}
            for value in data["queries"][provider].items():
                if value == "":
                    raise TweepError('Expected queries config data '
                                     'in config.js but found nothing')
                else:
                    config[value[0]] = value[1]
            return config

    @staticmethod
    def get_queries_collect_targets_config(provider):
        with open('config/config.json') as target_file:
            data = json.load(target_file)
            config = {}
            for value in data["queries"][provider]["collect_targets"].items():
                if value == "":
                    raise TweepError('Expected queries collect targets config '
                                     'in config.js but found nothing')
                else:
                    config[value[0]] = value[1]
            return config

    @staticmethod
    def get_patterns():
        with open('config/patterns.json') as target_file:
            data = json.load(target_file)
            patterns = {}
            for pattern in data.items():
                patterns[pattern[0]] = pattern[1]
            return patterns

    @staticmethod
    def get_patterns_by_target(target):
        with open('config/patterns.json') as target_file:
            data = json.load(target_file)
            extraction_patterns = []
            for pattern in data[target]["extraction_patterns"].items():
                if pattern == "":
                    raise TweepError('Expected ' + target + ' extraction patterns'
                                     ' in patterns.js but found nothing')
                else:
                    extraction_patterns.append(pattern)
            return extraction_patterns

    @staticmethod
    def get_export_config():
        with open('config/config.json') as target_file:
            data = json.load(target_file)
            locations = {}
            for location in data["export"].items():
                if location == "":
                    raise TweepError('Expected export to CSV dir location'
                                     'in config.js but found nothing')
                else:
                    locations[location[0]] = location[1]

            return locations