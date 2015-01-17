import datetime
from data.api.tinydb.api import TinyDBApi


class DataApi:

    _dbApi = None

    def __init__(self):
        self._dbApi = TinyDBApi()
        pass

    def get_all(self, name):
        return self._dbApi.get_db(name)

    def insert(self, target, item):
        return self._dbApi.get_db(target).insert(item)

    def insert_user(self, item):
        return self._dbApi.get_db("users").insert(item)

    def get_all_users_twitter_id(self):
        return [x["twitter_id"] for x in self._dbApi.get_db("users").all()]

    def insert_query_log(self, operation, target, last_processed_id):
        return self._dbApi.get_db("query_log").insert({
            "operation": operation,
            "target": target,
            "since_id": last_processed_id,
            "sent_timestamp": str(datetime.datetime.utcnow())
        })

    def update_query_log(self, items_fetched_count, unique_users_added_count, last_processed_id, eid):
        return self._dbApi.get_db("query_log").update(
            {
                'items_fetched_count': str(items_fetched_count),
                'unique_users_added_count': str(unique_users_added_count),
                'last_processed_id': str(last_processed_id),
                'processed_timestamp': str(datetime.datetime.utcnow()),
            }, eids=[eid])

    def search_queries(self, name, value):
        return self._dbApi.get_db("users").get(TinyDBApi.get_where()(name) == value)

    def update_process_log(self, last_processed_id, last_processed_id_eid):
        return self._dbApi.get_db("process_log").update(
            {
                'processed_timestamp': str(datetime.datetime.utcnow()),
                'last_processed_id': str(last_processed_id)
            }, eids=[last_processed_id_eid])

    def get_query_latest_processed_id(self, target):
        items = self._dbApi.get_db("process_log").search(TinyDBApi.get_where()("target") == target)
        if len(items) > 0:
            return items[0]["last_processed_id"], items[0].eid
        else:
            return "", self._dbApi.get_db("process_log").insert({
                'target': target,
                'processed_timestamp': str(datetime.datetime.utcnow()),
                'last_processed_id': ""
            })
