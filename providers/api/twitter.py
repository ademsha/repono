import datetime

from config.app import AppConfig

from data.api.api import DataApi
from providers.data.twitter import TwitterData
from providers.extraction.twitter.extractor import TwitterDataExtractor


class TwitterProviderApi:
    _dataApi = None
    _twitterData = None
    _patterns = {}
    _twitterDataExtractor = None

    def __init__(self):
        self._dataApi = DataApi()
        self._twitterData = TwitterData()
        self._twitterDataExtractor = TwitterDataExtractor()
        self._patterns = AppConfig.get_patterns()
        pass

    def add_unique_users(self, users):
        no_users = 0
        for user in users:
            all_twitter_ids = self._dataApi.get_all_users_twitter_id()
            if all_twitter_ids.count(user["twitter_id"]) == 0:
                self._dataApi.insert_user(user)
                no_users += 1
        return no_users

    # noinspection PyBroadException
    def search_statuses(self, target):

        print "Collecting " + str.upper(target) + " data started // " + str(datetime.datetime.utcnow())

        # Get last processed Twitter status id
        last_processed_id, last_processed_id_eid = self._dataApi.get_query_latest_processed_id(target)

        # Add new query log record in database for this call
        qeid = self._dataApi.insert_query_log("search", target, last_processed_id)

        # Search Twitter and get statuses and users
        last_processed_id, items, users = self._twitterData.search(self._patterns[target]["search_pattern"],
                                                                   last_processed_id)

        print str(len(items)) + " new items added to " + str.upper(target) + " dataset"

        # Extract statuses and prepared items
        for item in items:
            self._dataApi.insert(target, self._twitterDataExtractor.extract(target, item))

        # Add unique users
        no_users = self.add_unique_users(users)

        print str(no_users) + " new unique users added"

        # Update last processed
        self._dataApi.update_process_log(last_processed_id, str(last_processed_id_eid))

        # Update query log record in database for this call
        self._dataApi.update_query_log(str(len(items)), no_users, last_processed_id, str(qeid))

        print "Collecting " + str.upper(target) + " data finished // " + str(datetime.datetime.utcnow())