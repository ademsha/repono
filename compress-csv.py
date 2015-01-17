import datetime

from export.compress import Compress


if __name__ == "__main__":

    print "Compressing of CSV files started // " + str(datetime.datetime.utcnow())

    Compress().compress_all_csv()

    print "Compressing of CSV files finished // " + str(datetime.datetime.utcnow())
