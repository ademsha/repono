from providers.extraction.twitter.patterns import TwitterPatternExtractor


class TwitterDataExtractor:
    def __init__(self):
        pass

    @staticmethod
    def prepare_item(extracted_data, raw_data):
        for data in extracted_data.items():
            raw_data[data[0]] = data[1]
        return raw_data

    @staticmethod
    def extract(target, raw_data):
        extracted_data = TwitterPatternExtractor(target).extract(raw_data["twitter_status"],
                                                                 raw_data["twitter_expanded_url"])
        return TwitterDataExtractor.prepare_item(extracted_data, raw_data)