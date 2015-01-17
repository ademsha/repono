# -*- coding: utf-8 -*-
import tweepy

from config.app import AppConfig


class TwitterData:

    _provider = None
    _config = None

    def __init__(self):
        consumer_key, consumer_secret = AppConfig().get_twitter_auth()
        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        self._provider = tweepy.API(auth)
        self._config = AppConfig.get_queries_config("twitter")
        pass

    def search(self, term, last_processed_id):
        tweets = self._provider.search(term,
                                       since_id=last_processed_id,
                                       count=int(self._config["search_status_count"]))
        items = []
        users = []
        new_last_processed_id = last_processed_id

        for tweet in tweets:

            new_last_processed_id = tweets[0].id

            twitter_expanded_url = ""
            if len(tweet.entities["urls"]) > 0:
                twitter_expanded_url = tweet.entities["urls"][0]["expanded_url"]
            item = {
                'twitter_status_id': unicode(tweet.id),
                'twitter_author_id': unicode(tweet.author.id_str),
                'twitter_status': unicode(tweet.text),
                'twitter_status_created_at': unicode(tweet.created_at),
                'twitter_expanded_url': twitter_expanded_url,
                'twitter_source': tweet.source
            }
            items.append(item)
            user = {
                'twitter_id': unicode(tweet.author.id_str),
                'twitter_created_at': unicode(tweet.author.created_at),
                'twitter_favourites_count': unicode(tweet.author.favourites_count),
                'twitter_followers_count': unicode(tweet.author.followers_count),
                'twitter_statuses_count': unicode(tweet.author.statuses_count),
                'twitter_friends_count': unicode(tweet.author.friends_count),
                'twitter_protected': unicode(tweet.author.protected),
                'twitter_lang': unicode(tweet.author.lang),
                'twitter_time_zone': unicode(tweet.author.time_zone),
                'twitter_utc_offset': unicode(tweet.author.utc_offset),
                'twitter_verified': unicode(tweet.author.verified)
            }
            users.append(user)

        return new_last_processed_id, items, {x['twitter_id']: x for x in users}.values()