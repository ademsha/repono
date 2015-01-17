# -*- coding: utf-8 -*-
import csv

from config.app import AppConfig
from data.api.api import DataApi
from helpers.files import FilesHelper


class ExportToCSV:

    _config = None
    _dataApi = None
    _target_dir_path = None

    def __init__(self):
        self._config = AppConfig.get_export_config()
        self._dataApi = DataApi()
        self._target_dir_path = self._config["csv"]["export_dir"]
        pass

    def export_all(self):
        FilesHelper.delete_all_contents_in_dir(self._target_dir_path)
        for target in AppConfig.get_queries_collect_targets_config("twitter").items():
            print "Exporting to CSV:", target[0]
            self.export(str(target[0]))
        print "Exporting to CSV: users"
        self.export("users")

    def export(self, target):
        target_file_path = self._target_dir_path + target + ".csv"
        with open(target_file_path, 'wb') as target_file:
            writer = csv.writer(target_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            counter = 1
            for item in self._dataApi.get_all(target).all():
                line = [counter]
                if target == "imdb":
                    line.append(item["rating"])
                    line.append(item["rating_max"])
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["release_year"]).encode("utf-8"))
                    line.append(item["url_id"])
                if target == "amazon":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(item["url_id"])
                if target == "youtube":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                    line.append(unicode(item["author"]).encode("utf-8"))
                if target == "yelp-reviews":
                    line.append(unicode(item["place"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                    line.append(unicode(item["review"]).encode("utf-8"))
                if target == "yelp-checkins":
                    line.append(unicode(item["place"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "vevo":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                    line.append(unicode(item["author"]).encode("utf-8"))
                    line.append(unicode(item["platform"]).encode("utf-8"))
                if target == "vimeo":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "tvshowtime":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["release_year"]).encode("utf-8"))
                    line.append(unicode(item["episode"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "spotify":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "pandora":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["artist"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "nike":
                    line.append(unicode(item["length"]).encode("utf-8"))
                    line.append(unicode(item["length_units"]).encode("utf-8"))
                    line.append(unicode(item["pace"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "lastfm":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["artist"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "goodreads-readings":
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["author"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "goodreads-ratings":
                    line.append(unicode(item["rating"]).encode("utf-8"))
                    line.append(unicode(item["rating_max"]).encode("utf-8"))
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["author"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "foursquare":
                    line.append(unicode(item["place"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target == "fandango":
                    line.append(unicode(item["rating"]).encode("utf-8"))
                    line.append(unicode(item["rating_max"]).encode("utf-8"))
                    line.append(unicode(item["title"]).encode("utf-8"))
                    line.append(unicode(item["url"]).encode("utf-8"))
                if target != "users":
                    line.append(item["twitter_author_id"])
                    line.append(item["twitter_status_id"])
                    line.append(unicode(item["twitter_status_created_at"]).encode("utf-8"))
                else:
                    line.append(item["twitter_id"])
                    line.append(unicode(item["twitter_created_at"]).encode("utf-8"))
                    line.append(item["twitter_favourites_count"])
                    line.append(item["twitter_followers_count"])
                    line.append(item["twitter_statuses_count"])
                    line.append(item["twitter_friends_count"])
                    line.append(item["twitter_protected"])
                    line.append(item["twitter_verified"])
                    line.append(unicode(item["twitter_lang"]).encode("utf-8"))
                    line.append(unicode(item["twitter_time_zone"]).encode("utf-8"))
                    line.append(unicode(item["twitter_utc_offset"]).encode("utf-8"))

                writer.writerow(line)
                counter += 1
