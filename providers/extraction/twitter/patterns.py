import re

from config.app import AppConfig


class TwitterPatternExtractor:

    extraction_patterns = []

    def __init__(self, target):
        self.extraction_patterns = AppConfig.get_patterns_by_target(target)

    def extract(self, status, url):
        result = {}
        for pattern in self.extraction_patterns:

            if pattern[0].__contains__("url"):
                value = url
            else:
                value = status

            po = re.compile(pattern[1], re.M | re.I)
            results = po.findall(value)
            if len(results) > 0:
                result[pattern[0]] = results[0]
            else:
                result[pattern[0]] = ""

        return result
