import datetime

from export.compress import Compress


if __name__ == "__main__":

    print "Compressing of DB files started // " + str(datetime.datetime.utcnow())

    Compress().compress_all_tinydb()

    print "Compressing of DB files finished // " + str(datetime.datetime.utcnow())
