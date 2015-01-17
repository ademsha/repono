# -*- coding: utf-8 -*-
import datetime
import sys

from config.app import AppConfig
from providers.api.twitter import TwitterProviderApi


if __name__ == "__main__":

    args = [x for x in sys.argv if x != "collect.py"]

    targets = AppConfig.get_queries_collect_targets_config("twitter").items()

    print "Started collecting Twitter data // " + str(datetime.datetime.utcnow())

    if args is not None and len(args) == 1 and args[0] == "all":
        for target in targets:
            if target[1]:
                TwitterProviderApi().search_statuses(str(target[0]))
    elif args is not None and len(args) > 0:
        for arg in args:
            if any([str(arg) == str(x[0]) for x in targets]):
                TwitterProviderApi().search_statuses(str(arg))
            else:
                print "Wrong argument provided or target data collection is not " \
                      "enabled (Hint: Check config.json settings)."
    else:
        print "No arguments/targets for collection provided."

    print "Finished collecting Twitter data // " + str(datetime.datetime.utcnow())
